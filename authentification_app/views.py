import uuid

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponse
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail

from authentification_app.auth_view_functions import *

def ls(request):
    u = request.user
    if u.is_authenticated:
        if u.is_active:
            basket_item_xs = request.POST.get('XS')
            basket_item_s = request.POST.get('S')
            basket_item_m = request.POST.get('M')
            basket_item_l = request.POST.get('L')
            basket_item_xl = request.POST.get('XL')
            print('CHOSEN BASKET ITEM ---- ', basket_item_xs, basket_item_s, basket_item_m, basket_item_l, basket_item_xl)
            userorders = user_orders(u)
            active_orders, finished_orders = userorders
            data = {'id': u.pk,
                    'username': u.username,
                    'first_name': u.first_name,
                    'last_name': u.last_name,
                    'email': u.email,
                    'money': u.money,
                    'active_orders': active_orders,
                    'finished_orders': finished_orders,
                    }
            return render(request, 'authentification_app/user_privat_account.html', data)
        else:
            return HttpResponse('Поздравляем вас добавили в игнор лист, вам запрещено у нас что-либо покупать')

    return HttpResponse('Erorrrrrr')


def password_change(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            password = request.POST.get('password')
            password_repeat = request.POST.get('password_repeat')

            errors = user_password_valid(password, password_repeat)
            print('ERRORS --- ', errors)

            if errors:
                user = AllUsers.objects.get(username=request.user)
                username = user.username
                data = {'errors': errors, 'username': username }
                return render(request, 'authentification_app/password_change_form.html', data)
            else:
                user = AllUsers.objects.get(username=request.user)
                user.password = make_password(password)
                user.save()
                data = {'done': 'done',}
                return render(request, 'authentification_app/password_change_form.html', data)


def delete_account(request):
    if request.user.is_authenticated:
        user = AllUsers.objects.get(username=request.user)
        user.delete()
        return render(request, 'authentification_app/deleted_account.html')
    else:
        return HttpResponse('User is not authenticated!!! ')


def user_login(request):
    user_is_None = {'err': 'Пользователь не найден'}
    if request.method == 'POST':
        if request.user.is_authenticated:
            user = AllUsers.objects.get(username=request.user)
            username = user.username
            if request.user.check_password(request.POST.get('password')):
                data = {'username': username}
                return render(request, 'authentification_app/password_change_form.html', data)
            else:
                data = {'error':'Вы неверно ввели пароль, попробуйте еще раз', 'username' : username }
                return render(request, 'authentification_app/user_privat_account.html', data)

        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            for u in AllUsers.objects.all():
                if email == u.email:
                    if u.check_password(request.POST.get('password')):
                        user = authenticate(username=u.username, password=password)
                        if user.is_active:
                            login(request, user)
                            userorders = user_orders(u)
                            active_orders, finished_orders = userorders
                            data = {'id': u.pk,
                                    'username': u.username,
                                    'first_name': u.first_name,
                                    'last_name': u.last_name,
                                    'email': u.email,
                                    'money': u.money,
                                    'active_orders': active_orders,
                                    'finished_orders': finished_orders,
                                    }
                            return render(request, 'authentification_app/user_privat_account.html', data)
        except Exception as err:
            print('Error auth --- ', err)
            return render(request, 'authentification_app/user_privat_account.html', user_is_None)

        return render(request, 'authentification_app/user_privat_account.html', user_is_None)
    else:
        u = request.user
        userorders = user_orders(u)
        active_orders, finished_orders = userorders
        data = {'id': u.pk,
                'username': u.username,
                'first_name': u.first_name,
                'last_name': u.last_name,
                'email': u.email,
                'money': u.money,
                'active_orders': active_orders,
                'finished_orders': finished_orders,
                }
        return render(request, 'authentification_app/user_privat_account.html',data)



def user_logout(request):
    logout(request)
    return render(request, 'bike_app/main_page.html', {'username': None})


# Вариант с произвольной формой

class User_Registration():
    username = ''
    first_name = ''
    last_name = ''
    email = ''
    password = ''
    code_for_registration = ''

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
            code_for_registration = str(uuid.uuid4())
            print('CODE FOR REGISTRATION ---', code_for_registration)
            send_mail(
                'Здравствуйте!!!',

                'Вас приветствует магазин BikeShop, код для продолжения регистрации {}, '
                'если вы у нас не регистрировались, '
                'то просто игнорируйте это сообщение'.format(code_for_registration),

                'Wind-of-fortune2@yandex.ru',
                [email],
                fail_silently=False,
            )

            User_Registration.username = username
            User_Registration.first_name = first_name
            User_Registration.last_name = last_name
            User_Registration.email = email
            User_Registration.password = password
            User_Registration.code_for_registration = code_for_registration

            return render(request, 'authentification_app/register_form.html', {'email_answer':'yes'})

    return render(request, 'authentification_app/register_form.html')


def user_register_part2(request):
    if request.method == 'POST':
        user_answer = request.POST.get('user_answer')
        print(str(User_Registration.code_for_registration))

        if user_answer == str(User_Registration.code_for_registration):
            newuser = AllUsers(username=User_Registration.username,
                               first_name=User_Registration.first_name,
                               last_name=User_Registration.last_name,
                               email=User_Registration.email,
                               password=make_password(User_Registration.password),
                               date_joined=timezone.now()
                               )
            newuser.save()

            user = authenticate(username=User_Registration.username, password=User_Registration.password)
            login(request, user)
            userorders = user_orders(user)
            active_orders, finished_orders = userorders
            data = {'id': user.pk,
                    'username': user.username,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'email': user.email,
                    'money': user.money,
                    'active_orders': active_orders,
                    'finished_orders': finished_orders,
                    }
            return render(request, 'authentification_app/user_privat_account.html', data)
        else:
            data = {'mistake':'uncorrect_email_answer'}
            return render(request, 'authentification_app/register_form.html', data)

def user_active_orders(request):
    u = request.user
    order_id = ''
    if u.is_authenticated:
        if u.is_active:
            try:
                order_id = request.get_full_path()
                print('ORDER _ID ---', order_id)
                order_id = order_id.split('?')
                order_id = int(order_id[-1])
                print('ORDER _ID2 ---', order_id)
            except Exception as e:
                print('EXCEPTION ---', e)

            if type(order_id) == int :
                order = Order.objects.get(id=order_id)
                order.is_active = False
                order.is_paid = True
                order.date_delivered = timezone.now()
                order.add_information = ' '
                order.save()

                active_orders = []
                for i in Order.objects.filter(username=u.username):
                    if i.is_active == True:
                        active_orders.append(i)
                active_orders.reverse()

                change_orders_view(active_orders)

                data = {'username': u.username,
                        'active_orders': active_orders
                        }
                return render(request, 'authentification_app/user_active_orders.html', data)
            else:

                active_orders = []
                for i in Order.objects.filter(username=u.username):
                    if i.is_active == True:
                        active_orders.append(i)
                active_orders.reverse()

                change_orders_view(active_orders)

                data = {'username': u.username,
                        'active_orders': active_orders
                        }
                return render(request, 'authentification_app/user_active_orders.html', data)
    return HttpResponse('user_active_orders - error')


def user_finished_orders(request):
    u = request.user
    if u.is_authenticated:
        if u.is_active:
            finished_orders = []
            for i in Order.objects.filter(username=u.username):
                if i.is_active == False:
                    finished_orders.append(i)
            finished_orders.reverse()

            change_orders_view(finished_orders)

            data = {'username': u.username,
                    'finished_orders': finished_orders
                    }
            return render(request, 'authentification_app/user_finished_orders.html', data)
    return HttpResponse('user_finished_orders - error')




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
