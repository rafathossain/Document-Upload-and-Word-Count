FROM python:3.9.2

RUN apt-get -y update \
    && apt-get install -y \
    python3-pip libffi-dev gcc default-libmysqlclient-dev \
    && apt-get -y clean

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

COPY deployment/* /app/deployment/*
RUN sed -i 's/\r$//g' /app/deployment/*
RUN chmod +x /app/deployment/*

ENTRYPOINT ["/app/deployment/entrypoint"]