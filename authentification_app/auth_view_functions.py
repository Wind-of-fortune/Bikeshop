import uuid

from django.core.validators import validate_email
from django.core.mail import send_mail
from django.core.exceptions import ValidationError

from authentification_app.models import AllUsers
from order_app.models import *

# Валидация
def user_registration_valid (username, first_name, last_name, email, password, password2):
    errors = []
    print('EMAIL', email)

    try:
        if AllUsers.objects.get(email=email):
            errors.append('Извините, но email по которому вы регистрируетесь уже занят')
    except Exception as e:
        print('Email Error --- ', e)



    try:
        if AllUsers.objects.get(username=username):
            errors.append('Извините, но пользователь с таким именем уже существует')
    except Exception as e:
        print('Username Error --- ', e)



    try:
        if username == '':
            errors.append('Извините, но username необходимое для ввода поле')

        if email == '':
            errors.append('Извините, но email необходимое для ввода поле')

        if password == '':
            errors.append('Извините, но password необходимое для ввода поле')

        if password != password2:
            errors.append('Вы ввели разные пароли, будьте внимательней')

        if len(username) > 30:
            errors.append('Извините, но длинна имени пользователя не может превышать 30 символов')
        if len(first_name) > 30:
            errors.append('Извините, но длинна имени не может превышать 30 символов')
        if len(last_name) > 50:
            errors.append('Извините, но длинна фамилий не может превышать 50 символов')
        if len(email) > 100:
            errors.append('Извините, но длинна email не может превышать 100 символов')
        if len(password) > 100:
            errors.append('Извините, но длинна password не может превышать 100 символов')
        if len(password) < 4:
            errors.append('Извините, password слишком короткий, введите более длинный password')

        try:
            validate_email(email)
        except ValidationError as e:
            errors.append('Email введен некорректно')
            return errors

        return errors

    except Exception as e:
        print('Somethin goes wrong ---- ',e)
        return 'except'


def user_password_valid (password, password2):
    errors = []

    if len(password) > 100:
        errors.append('Извините, но длинна password не может превышать 100 символов')
    if len(password) < 4:
        errors.append('Извините, password слишком короткий, введите более длинный password')
    if password != password2:
        errors.append('Вы ввели разные пароли, будьте внимательней')

    return errors

def user_orders(user):
    active_orders = []
    finished_orders = []
    for i in Order.objects.filter(username=user.username):
        if i.is_active == True:
            active_orders.append(i)
        if i.is_active == False:
            finished_orders.append(i)
    return active_orders, finished_orders