from celery import Celery

from sms import send_sms


app = Celery('tasks', broker='redis://redis:6379/0', backend='redis://redis:6379/0')


@app.task()
def send_message(msg, phone):
    send_sms(msg, phone)
