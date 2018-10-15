# Install python
FROM python:3.6

WORKDIR /

COPY api/ /api

ADD requirements.txt /

RUN python api/wsgi.py

RUN pip install -r requirements.txt
