FROM python:3.8

ENV PYTHONUNBUFFERED=1

RUN mkdir /app
WORKDIR /app

ADD requirements.txt ./
RUN pip install -r requirements.txt

ADD ./korero .
