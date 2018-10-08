from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from authentification_app.models import AllUsers

# Валидация
def user_registration_valid (username, first_name, last_name, email, password, password2):
    errors = []
    for u in AllUsers.objects.all():
        try:
            if username == '':
                errors.append('Извините, но username необходимое для ввода поле')
            if email == '':
                errors.append('Извините, но email необходимое для ввода поле')
            if password == '':
                errors.append('Извините, но password необходимое для ввода поле')
            if username == u.username:
                errors.append('Извините, но пользователь с таким именем уже существует')
            if email == u.email:
                errors.append('Извините, но email по которому вы регистрируетесь уже занят')
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
        except Exception as e:
            print('Somethin goes wrong ---- ',e)
            return 'except'