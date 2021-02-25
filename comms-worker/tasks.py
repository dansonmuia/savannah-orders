from celery import Celery
from celery.utils.log import get_task_logger

from sms import send_sms


app = Celery('tasks', broker='redis://redis:6379/0', backend='redis://redis:6379/0')

logger = get_task_logger(__name__)


@app.task()
def send_message(msg, phone):
    send_sms(msg, phone)
    logger.info('Attempted to send sms')
