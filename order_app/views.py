import json

from django.shortcuts import render
from django.http import HttpResponse

from order_app.models import *

def basket(request):
    pressed=''
    try:
        pressed = request.get_full_path()
        pressed = pressed.split('del')
        pressed = int(pressed[1][0])
    except Exception as e:
        print('EXCEPTION ---', e)

    u = request.user
    data = {'username': u.username}

    if type(pressed) == int:  #delete items from basket
        if u.is_authenticated:
            if u.is_active:
                item_to_delete = Basket.objects.get(id=pressed)
                item_to_delete.delete()
                order_id = []
                orders = []

                for i in Basket.objects.all():
                    if i.username == u.username:
                        order_id.append(i.pk)

                for i in order_id:
                    o = Basket.objects.get(pk=i)
                    orders.append(o)
                print(orders)

                data = {'username': u.username, 'orders': orders}

                return render(request, 'order_app/basket.html', data)

    if u.is_authenticated: #view items in basket
        if u.is_active:
            order_id=[]
            orders =[]

            for i in Basket.objects.all():
                if i.username == u.username:
                    order_id.append(i.pk)

            for i in order_id:
                o = Basket.objects.get(pk=i)
                orders.append(o)
            print(orders)

            data = {'username': u.username, 'orders': orders,}
            return render(request, 'order_app/basket.html', data)
    return HttpResponse('Проблема с авторизацией')


class OrderNotes():
    item_id = ''

def make_order(request):
    if request.method == 'POST':
        u = request.user
        if u.is_authenticated:
            if u.is_active:
                country = request.POST.get('country')
                city = request.POST.get('city')
                street = request.POST.get('street')
                house = request.POST.get('house')
                postcode = request.POST.get('postcode')
                phone = request.POST.get('phone')
                try:
                    item = Basket.objects.get(id=OrderNotes.item_id)
                except Exception as e:
                    return HttpResponse('There is no that item in the basket')
                


    pressed = ''
    try:
        pressed = request.get_full_path()
        pressed = pressed.split('add')
        pressed = int(pressed[1][0])
    except Exception as e:
        print('EXCEPTION ---', e)

    u = request.user
    data = {'username': u.username}
    if type(pressed) == int:  #view items in basket
        if u.is_authenticated:
            if u.is_active:
                item = Basket.objects.get(id=pressed)
                OrderNotes.item_id = pressed
                data = {'username': u.username, 'item': item,}
                return render(request, 'order_app/order_notes.html', data)
    return HttpResponse('Проблема с авторизацией')