FROM python:3.9-slim

WORKDIR /usr/src/app/backend

ENV LANG=C.UTF-8

COPY ./requirements.txt .

RUN apt-get update; \
    apt-get install -y --no-install-recommends \
    default-libmysqlclient-dev \
    gcc \
    git \
    openssh-client \
    wget \
    ; \
    apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false; \
    apt-get clean; \
    rm -rf /var/lib/apt/lists/* \
    ; \
    \
    python -m pip install --upgrade pip; \
    pip install --no-cache-dir --upgrade -r ./requirements.txt \
    ; \
    \
    useradd -m -s /bin/bash dev
