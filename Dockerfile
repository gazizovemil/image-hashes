FROM python:3.10-alpine

WORKDIR /opt/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
CMD ["flask", "run"]
