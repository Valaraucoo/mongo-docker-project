FROM python:3.10.4-alpine

WORKDIR app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY client client/
