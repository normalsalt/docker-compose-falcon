# Falcon Framework API

## Python version

- python:3.8.5-alpine

Update `Dockerfile`.

# up

```
docker-compose up -d
```

Open `http://localhost:8000/quote` in your browser; you'll see this output:

```
{"quote": "I've always been more interested in the future than in the past.", "author": "Grace Hopper"}
```

# test

```
docker-compose run --rm python python -m unittest
```

# Falcon Framework

https://falconframework.org/

## Falcon version

- falcon>=2.0.0,<3.0.0
- gunicorn>=20.0.4,<21.0.0

Update `requirements.txt`.

## documentation

https://falcon.readthedocs.io/en/stable/

# build

```
docker-compose up -d --build
```
