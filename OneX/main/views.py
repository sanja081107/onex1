from datetime import datetime, timedelta

from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response

from .permissions import *
from .serializers import *
from .service import TransactionFilter

"""Просмотр список пользователей"""
class UserListAPIList(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UserListSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


"""Просмотр своего профиля"""
class UserMeDetailAPIView(generics.ListAPIView):
    serializer_class = UserListSerializer

    def get_queryset(self):
        pk = self.request.user.pk
        if pk:
            return Users.objects.filter(pk=pk)
        return Users.objects.all()


"""Просмотр и изменение пользователя"""
class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = (IsOwner, )


"""Создать транзакцию"""
class TransactionAPIView(generics.CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


"""Показывает все наши транзакции"""
class TransactionListAPIView(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionListSerializer
    filter_backends = (DjangoFilterBackend,)        # http://127.0.0.1:8000/api/v1/transaction/me/?date_after=2022-11-06&date_before=2022-11-07
    filterset_class = TransactionFilter             # http://127.0.0.1:8000/api/v1/transaction/me/?sum_min=50&sum_max=200

    def get_queryset(self):
        user = self.request.user
        if user:
            return Transaction.objects.filter(user=user)
        return Transaction.objects.all()


"""Просмотр баланса пользователя"""
class BalanceAPIView(generics.ListAPIView):
    serializer_class = BalanceSerializer

    def get_queryset(self):
        user = self.request.user
        if user:
            return Balance.objects.filter(user=user)
        return Balance.objects.all()


"""Изменение баланса пользователя"""
class UpdateBalanceAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = UpdateBalanceSerializer
    permission_classes = (IsOwnerOnly,)
    queryset = Balance.objects.all()


"""Просмотр категорий"""
class CategoryListAPIView(generics.ListAPIView):
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()


"""Изменение категорий"""
class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()


"""Просмотр статистики"""
class StatisticAPIView(APIView):

    def get(self, request):
        today = datetime.date(datetime.now())
        yesterday = today - timedelta(days=1)

        posts_yesterday = Transaction.objects.filter(user=self.request.user, date=yesterday)
        posts_today = Transaction.objects.filter(user=self.request.user, date=today)

        if posts_today:
            list_today = [f'{el.sum}p. date: {el.date}' for el in posts_today]
        else:
            list_today = 'No posts today'

        if posts_yesterday:
            list_yesterday = [f'{el.sum}p. date: {el.date}' for el in posts_yesterday]
        else:
            list_yesterday = 'No posts yesterday'

        return Response({
                        'Your transaction for today': list_today,
                        'Your transaction for yesterday': list_yesterday,
                        })
