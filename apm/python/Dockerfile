FROM python:3.9 AS builder
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./src .


CMD [ "python", "./app.py" ]