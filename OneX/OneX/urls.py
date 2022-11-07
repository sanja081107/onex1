"""OneX URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),

    # аутентификация по session
    path('auth-session/', include('rest_framework.urls')),

    # аутентификация по token
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    # http://127.0.0.1:8000/auth/token/login/       для авторизации
    # http://127.0.0.1:8000/auth/token/logout/      для выхода
    # http://127.0.0.1:8000/auth/users/             для регистрации и простора всех пользователей
    # http://127.0.0.1:8000/auth/users/activation/  для активации регистрации по почте
    # http://127.0.0.1:8000/auth/users/me           для просмотра своего профиля

    # аутентификация по jwt token
    path('auth-jwt/', include('djoser.urls.jwt')),

    path('', include('main.urls')),
]
