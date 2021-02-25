FROM python:3.6

RUN mkdir -p /orders-app

WORKDIR /orders-app

COPY . ./

RUN pip install -r requirements/requirements.txt

RUN flask db upgrade

ENV FLASK_ENV=development

CMD flask run --host=0.0.0.0
