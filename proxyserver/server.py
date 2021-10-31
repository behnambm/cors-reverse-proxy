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

        if self.path == '/api/get-count/':
            # if user wants to get `count` value
            # this will inject a new header `Authorization` to headers
            headers = {
                'Authorization': '123456',
            }
            resp = requests.get(
                url='http://localhost:8000/api/get-count/',
                headers=headers,
            )
            self.wfile.write(json.dumps(resp.json()).encode('utf-8'))

        else:
            resp = requests.get(
                'http://localhost:8000' + self.path,
            )
            self.wfile.write(json.dumps(resp.json()).encode('utf-8'))

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Max-Age', '86400')
        self.send_header('Access-Control-Allow-Method', 'POST, GET, OPTIONS')
        self.end_headers()

        if self.path == '/api/add-one/':
            # if user wants to increase `count` by one
            # this will inject a new header `Authorization` to headers
            headers = {
                'Authorization': '123456',
            }
            resp = requests.post(
                url='http://localhost:8000/api/add-one/',
                headers=headers,
            )
            self.wfile.write(json.dumps(resp.json()).encode('utf-8'))

        else:
            resp = requests.post(
                'http://localhost:8000' + self.path,
            )
            self.wfile.write(json.dumps(resp.json()).encode('utf-8'))

try:
    httpd = socketserver.TCPServer(('', 9090), MyProxy)
    print('listening on port 9090...')
    httpd.serve_forever()
except:
    print('closing connection...')
    httpd.server_close()
