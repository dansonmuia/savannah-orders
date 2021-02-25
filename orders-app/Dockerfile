FROM python:3.6

RUN mkdir -p /orders-app

WORKDIR /orders-app

COPY . ./

RUN pip install -r requirements/requirements.txt

ENV SECRET_KEY=${SECRET_KEY}

ENV POSTGRES_DB=${POSTGRES_DB}
ENV POSTGRES_USER=${POSTGRES_USER}
ENV POSTGRES_PASSWORD=${POSTGRES_PASSWORD}


CMD flask fly-init-db && flask db upgrade && flask run --host=0.0.0.0
