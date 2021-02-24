from celery import Celery


celery_app = Celery('tasks', broker='redis://redis:6379/0', backend='redis://redis:6379/0')


def send_confirm_order_sms(order):
    msg = f'{order.customer.full_name} we have received your order for {order.item}, {order.amount} amount'
    kwargs = {
        'msg': msg,
        'phone': order.customer.phone
    }

    celery_app.send_task('tasks.send_message', kwargs=kwargs)
