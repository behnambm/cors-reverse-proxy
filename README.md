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


## Diagrams

`/api/echo/`

![echo](https://user-images.githubusercontent.com/26994700/139604545-7f2154a9-b551-44b7-9d94-ecb5f1152727.png)

---

`/api/get-count/`

![get-count](https://user-images.githubusercontent.com/26994700/139604552-90cea5c3-a1ff-4536-a023-dbe305616181.png)

---

`/api/add-one/`

![increase-count](https://user-images.githubusercontent.com/26994700/139604554-f36bb44c-fdbf-455a-b61e-97b47d8672ef.png)


