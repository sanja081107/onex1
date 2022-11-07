from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    path('api/v1/users/', UserListAPIList.as_view()),                       # для просмотра пользователей get
    path('api/v1/users/me/', UserMeDetailAPIView.as_view()),                # для просмотра своего профиля get
    path('api/v1/users/<int:pk>/', UserDetailAPIView.as_view()),            # для просмотра своего профиля get,put,delete
    path('api/v1/transaction/', TransactionAPIView.as_view()),              # для проведения транзакции post
    path('api/v1/transaction/me/', TransactionListAPIView.as_view()),       # для просмотра своих транзакций get
    path('api/v1/my_balance/', BalanceAPIView.as_view()),                   # для просмотра своего баланса get
    path('api/v1/my_balance/<int:pk>/', UpdateBalanceAPIView.as_view()),    # для изменения своего баланса get,put,delete
    path('api/v1/category/', CategoryListAPIView.as_view()),                # для просмотра категорий get
    path('api/v1/category/<int:pk>/', CategoryDetailAPIView.as_view()),     # для изменения категории get,put,delete
    path('api/v1/statistic/', StatisticAPIView.as_view()),                  # для просмотра статистики get
]
