from http import server
import socketserver
import json
import requests


class MyProxy(server.BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        """
        This is used for handling pre-flight requests that browser makes for 
        complex requests.
        
        """
        self.send_response(204)  # no content
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Max-Age', '86400')
        self.send_header('Access-Control-Allow-Method', 'POST, GET, OPTIONS')
        self.end_headers()

    def do_GET(self):
        self.send_response(200, 'test')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Max-Age', '86400')
        self.send_header('Access-Control-Allow-Method', 'POST, GET, OPTIONS')
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        resp = requests.get('http://localhost:8000' + self.path)
        self.wfile.write(json.dumps(resp.json()).encode(encoding='utf_8'))


try:
    httpd = socketserver.TCPServer(('', 9090), MyProxy)
    print('listening on port 9090...')
    httpd.serve_forever()
except:
    print('closing connection...')
    httpd.server_close()
