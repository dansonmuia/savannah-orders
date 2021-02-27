FROM python:3.6

RUN mkdir -p /orders-app

WORKDIR /orders-app

COPY . ./

RUN pip install -r requirements/requirements.txt


CMD flask fly-init-db && flask db upgrade && flask run --host=0.0.0.0
