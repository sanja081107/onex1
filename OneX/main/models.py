from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Transaction(models.Model):
    sum = models.PositiveIntegerField(default=0, verbose_name='Сумма')
    date = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, verbose_name='Категория')
    organisation = models.CharField(max_length=100, blank=True, verbose_name='Название организации')
    description = models.TextField(blank=True, verbose_name='Описание')
    user = models.ForeignKey('Users', on_delete=models.CASCADE, verbose_name='Пользователь')

    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'
        ordering = ['-date']

    def __str__(self):
        return f'{self.user} {self.sum} p.'


class Category(models.Model):
    title = models.CharField(unique=True, max_length=100, verbose_name='Название категории')

    class Meta:
        verbose_name = 'Категоря'
        verbose_name_plural = 'Категории'
        ordering = ['title']

    def __str__(self):
        return f'{self.title}'


class Balance(models.Model):
    balance = models.IntegerField(default=0, verbose_name='Баланс')
    user = models.ForeignKey('Users', on_delete=models.CASCADE, verbose_name='Пользователь')

    class Meta:
        verbose_name = 'Баланс'
        verbose_name_plural = 'Балансы'

    def __str__(self):
        return f'{self.balance}'
