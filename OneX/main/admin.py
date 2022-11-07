from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UsersCreationForm, UsersChangeForm
from .models import *

class UsersAdmin(UserAdmin):
    add_form = UsersCreationForm
    form = UsersChangeForm
    model = Users
    list_display = ['username', 'first_name', 'last_name', 'email']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


class BalanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'balance', 'user')


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'sum')


admin.site.register(Users, UsersAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Balance, BalanceAdmin)

