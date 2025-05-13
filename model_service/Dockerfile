# model_service/Dockerfile

FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["bentoml", "serve", "service:svc", "--port", "3000"]

