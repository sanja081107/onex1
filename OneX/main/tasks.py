from datetime import datetime, timedelta

from celery import shared_task
from django.core.mail import send_mail
from .models import Users, Transaction
import json


@shared_task(name='order_created')
def order_created(arg):
    """
    Задача для отправки уведомления по электронной почте
    """
    user_id = arg
    user = Users.objects.get(id=user_id)

    today = datetime.date(datetime.now())
    yesterday = today - timedelta(days=1)

    posts_yesterday = Transaction.objects.filter(user=user, date=yesterday)
    posts_today = Transaction.objects.filter(user=user, date=today)

    if posts_today:
        list_today = [f'{el.sum}p. date: {el.date}' for el in posts_today]
    else:
        list_today = 'No posts today'

    if posts_yesterday:
        list_yesterday = [f'{el.sum}p. date: {el.date}' for el in posts_yesterday]
    else:
        list_yesterday = 'No posts yesterday'

    message = f"'Your transaction for today': \n   {list_today}\n" \
              f"'Your transaction for yesterday': \n   {list_yesterday}"

    subject = 'Утренняя статистика'
    send_mail(subject,
              message,
              'sanja081107@gmail.com',
              [user.email]
              )

    return json.dumps({user.username: f'sending statistic for {datetime.date(datetime.now())} successfully'})
