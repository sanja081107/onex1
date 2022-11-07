from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *

class UsersCreationForm(UserCreationForm):

    class Meta:
        model = Users
        fields = ('username', 'email')

class UsersChangeForm(UserChangeForm):

    class Meta:
        model = Users
        fields = ('username', 'email')


# def user(request):
#     return request.user
#
#
# class MyForm(forms.ModelForm):
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['category'].queryset = Category.objects.filter(user=user)
#
#     class Meta:
#         model = Transaction
#         fields = ['category']
