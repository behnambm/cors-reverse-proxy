# cors-reverse-proxy

A simple reverse proxy in python to handle CORS headers & pre-flight requests

<br>

## Run Next.js app

First, run the development server:

```bash
cd frontend

npm run dev
# or
yarn dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

<br>

### Run Django API

```bash
cd backend

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Note: It's recommended to use `virtuale environment` in order to keep your system clean.

<br>

### Run proxy server

```bash
cd proxyserver
python server.py
```

This server will be listening on port `9090` & redirect all get requests to `http://localhost:8000/` and then return te response to client. Also the `OPTIONS` method is handled and will return required headers for CORS.
