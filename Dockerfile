FROM python:3.10-alpine

WORKDIR /opt/app

COPY . .

CMD ["python", "main.py"]
