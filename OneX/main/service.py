import json
from datetime import datetime

from django_celery_beat.models import PeriodicTask, IntervalSchedule, CrontabSchedule
from djoser.conf import settings
from django.db import transaction
from djoser.serializers import UserCreateSerializer
from django_filters import rest_framework as filters
from .models import *


category = [
    'Забота о себе', 'Зарплата', 'Здоровье и фитнес', 'Кофе и рестораны', 'Машина',
    'Образование', 'Отдых и развлечения', 'Платежи, комиссия', 'Покупки: одежда, техника',
    'Продукты', 'Проезд'
]


class TransactionFilter(filters.FilterSet):
    date = filters.DateFromToRangeFilter()
    sum = filters.RangeFilter()

    class Meta:
        model = Transaction
        fields = ['sum', 'date']


class SpecialUserCreateSerializer(UserCreateSerializer):

    def perform_create(self, validated_data):
        with transaction.atomic():
            user = Users.objects.create_user(**validated_data)
            if settings.SEND_ACTIVATION_EMAIL:
                user.is_active = False
                user.save(update_fields=["is_active"])

        for el in category:
            Category.objects.get_or_create(title=el)

        Balance.objects.create(balance=0, user=user)

        PeriodicTask.objects.create(
            name=f'statistic for {user.username}',
            task='order_created',
            crontab=CrontabSchedule.objects.get(day_of_week='1,2,3,4,5', hour='9', minute='0'),
            # interval=IntervalSchedule.objects.get(every=10, period='seconds'),
            args=json.dumps([user.id]),
            start_time=datetime.now(),
            one_off=False)
        return user
