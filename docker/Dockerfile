FROM python:alpine

WORKDIR /usr/src/myapp

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /workdir
