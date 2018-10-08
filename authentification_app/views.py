import uuid

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.http.response import HttpResponse, JsonResponse
from authentification_app.forms import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth import get_user
from django.utils import timezone
from django.shortcuts import get_object_or_404

from authentification_app.auth_view_functions import *

def get_token():
    return str(uuid.uuid4())


def user_login(request):
    user_is_None = {'err': 'Пользователь не найден'}
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            for u in AllUsers.objects.all():
                if email == u.email:
                    if u.check_password(request.POST.get('password')):
                        user = authenticate(username=u.username, password=password)
                        if user.is_active:
                            login(request, user)
                            data = {'id': u.pk,
                                    'username': u.username,
                                    'first_name': u.first_name,
                                    'last_name': u.last_name,
                                    'email': u.email,
                                    'money': u.money,
                                    }
                            return render(request, 'authentification_app/user_privat_account.html', data)
        except Exception as err:
            print('Error auth --- ', err)
            return render(request, 'authentification_app/user_privat_account.html', user_is_None)

        return render(request, 'authentification_app/user_privat_account.html', user_is_None)
    else:
        u = request.user
        data = {'id': u.pk,
                'username': u.username,
                'first_name': u.first_name,
                'last_name': u.last_name,
                'email': u.email,
                'money': u.money,
                }
        return render(request, 'authentification_app/user_privat_account.html',data)



def user_logout(request):
    logout(request)
    return render(request, 'bike_app/main_page.html', {'username': None})


# Вариант с произвольной формой
def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_repeat = request.POST.get('password_repeat')

        errors = user_registration_valid(username, first_name, last_name, email, password, password_repeat)
        print('ERRORS --- ',errors)
        if errors == 'except':
            return render(request, 'authentification_app/register_form.html')
        if errors:
            data = { 'errors': errors}
            return render(request, 'authentification_app/register_form.html', data)
        else:
            newuser = AllUsers(username=username,
                               first_name=first_name,
                               last_name=last_name,
                               email=email,
                               password=make_password(password),
                               token=get_token(),
                               date_joined=timezone.now()
                               )
            newuser.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            data = {'id': user.pk,
                    'username': user.username,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'email': user.email,
                    'money': user.money,
                    }
            print('DATA  ===  ', data)
            return render(request, 'authentification_app/user_privat_account.html', data)
    return render(request, 'authentification_app/register_form.html')


# # Вариант с формочкой
# def user_register(request):
#     data = {}
#     data['form'] = UserRegistartionForm()
#     if request.method == 'POST':
#         error = 'Вы ввели некорректные данные или ошиблись при вводе. Попробуйте зарегистрироваться снова'
#         new_user_form = UserRegistartionForm(request.POST)
#         if new_user_form.is_valid():
#             new_user_form.save(commit=False)
#             newuser = authenticate(username=new_user_form.cleaned_data['username'],
#                                    password=new_user_form.cleaned_data['password'])
#             login(request, newuser)
#             data = {'id': newuser.pk,
#                     'username': newuser.username,
#                     'first_name': newuser.first_name,
#                     'last_name': newuser.last_name,
#                     'email': newuser.email,
#                     'money': newuser.money,
#                     }
#             return render(request, 'authentification_app/user_privat_account.html', data)
#         else:
#             data['error'] = error
#             return render(request, 'authentification_app/register_form.html', data)
#     return render(request, 'authentification_app/register_form.html', data)
#
