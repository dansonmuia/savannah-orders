FROM python:3.6

RUN mkdir -p /worker

COPY . /worker

WORKDIR /worker

RUN pip install -r requirements.txt

ENTRYPOINT celery -A tasks worker --loglevel=info
