from rest_framework import serializers

from .models import *


class CategoryListSerializer(serializers.ModelSerializer):
    """Вывод списка актеров и режиссеров"""
    class Meta:
        model = Category
        fields = ("id", "title")


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'username', 'email')


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'username', 'first_name', 'last_name', 'email')


class TransactionSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Transaction
        fields = ('sum', 'date', 'category', 'organisation', 'description', 'user')

    def save(self, **kwargs):
        end = super(TransactionSerializer, self).save()
        user = self.context['request'].user
        summa = self.context['request'].POST['sum']
        balance = Balance.objects.get_or_create(user=user)
        end_sum = balance[0].balance - int(summa)
        balance[0].balance = end_sum
        balance[0].save()
        return end


class TransactionListSerializer(serializers.ModelSerializer):
    category = CategoryListSerializer(read_only=True)
    user = UserListSerializer(read_only=True)

    class Meta:
        model = Transaction
        fields = ('sum', 'date', 'category', 'organisation', 'description', 'user')


class BalanceSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Balance
        fields = "__all__"


class UpdateBalanceSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    balance = serializers.IntegerField(label='Сумма обновления')

    class Meta:
        model = Balance
        exclude = ('id',)

