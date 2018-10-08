from django.forms.models import ModelForm
from django.forms import forms, Widget, TextInput
from django.db import models
from django import forms
from authentification_app.models import AllUsers
from django.contrib.auth import  password_validation
from django.utils.translation import gettext, gettext_lazy as _


class UserRegistartionForm(forms.ModelForm):
    username = forms.CharField(max_length=30,
                               widget=forms.TextInput(attrs={'class':'form-control'}), label='Имя пользователя')
    first_name = forms.CharField(max_length=30,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}), label='Имя')
    last_name = forms.CharField(max_length=40,
                                widget=forms.TextInput(attrs={'class': 'form-control'}), label='Фамилия')
    email = forms.EmailField(max_length=100,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}), label='Email')
    password = forms.CharField(max_length=128, strip=False,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Пароль')
    password2 = forms.CharField(max_length=128, strip=False,
                                 widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Повторите пароль')
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }

    class Meta:
        model = AllUsers
        fields = ('username', 'email')


