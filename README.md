# cors-reverse-proxy

A simple reverse proxy in python to handle CORS headers & pre-flight requests.

And inject `Authorization` header to requests.

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

start your `redis-server` on `127.0.0.1:6379`

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

## Diagrams

`/api/echo/`

![echo](https://user-images.githubusercontent.com/26994700/139604723-4ea95003-c4e0-47b5-9302-e2fcb19e21b7.png)

---

`/api/get-count/`

![get-count](https://user-images.githubusercontent.com/26994700/139604728-1c7586d6-a5ca-4051-ae40-ca8f4a46d459.png)

---

`/api/add-one/`

![increase-count](https://user-images.githubusercontent.com/26994700/139604736-68a12618-b285-477f-8244-02bbd2cdc98d.png)
