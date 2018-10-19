import json

from django.shortcuts import render
from django.http import HttpResponse

from order_app.order_app_view_functions import *

class OrderNotes(): # I don't know how it would work with many users in the same time when they ordering
    item_id = ''    # diferent items. We should test this
    order_id = ''
    item = ''

    items_order_all = ''
    price_all = ''


def basket(request):
    pressed=''
    try:
        pressed = request.get_full_path()
        pressed = pressed.split('del')
        pressed = int(pressed[-1])
    except Exception as e:
        print('EXCEPTION ---', e)

    u = request.user
    delete_all_todelete_from_basket(u)

    if type(pressed) == int:  #delete items from basket
        if u.is_authenticated:
            if u.is_active:
                try:
                    item_to_delete = Basket.objects.get(id=pressed)
                    item_to_delete.delete()
                except Exception as e:
                    print('NO ITEMS  ----- ', e)

                order_id = []
                orders = []
                for i in Basket.objects.filter(username=u.username):
                    order_id.append(i.pk)

                if order_id == []: # check is basket empty or not
                    data = {'username': u.username, 'no_orders': None}
                    return render(request, 'order_app/basket.html', data)

                for i in order_id:
                    o = Basket.objects.get(pk=i)
                    orders.append(o)

                data = {'username': u.username, 'orders': orders}

                return render(request, 'order_app/basket.html', data)

    if u.is_authenticated: #view items in basket
        if u.is_active:
            order_id=[]
            orders =[]

            for i in Basket.objects.filter(username=u.username):
                order_id.append(i.pk)

            for i in order_id:
                o = Basket.objects.get(pk=i)
                orders.append(o)

            data = {'username': u.username, 'orders': orders,}
            return render(request, 'order_app/basket.html', data)
    return HttpResponse('Проблема с авторизацией')


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
                errors = valid_data_from_user(country,city,street,house,postcode,phone) # check user data
                if len(errors) > 0:
                    data = {'username': u.username, 'item': OrderNotes.item, 'errors': errors}
                    return render(request, 'order_app/order_notes.html', data)
                try:
                    item = Basket.objects.get(id=OrderNotes.item_id)
                    item.mark = 'to_delete'
                    item.save()

                    order = Order(username=item.username,
                                  order_item_name=item.item_name,
                                  order_item_size=item.item_size,
                                  items_price=str(item.item_price),
                                  sum_price=int(item.item_price),
                                  ship_country=country,
                                  ship_city=city,
                                  ship_street=street,
                                  ship_house=house,
                                  ship_postalcode=postcode,
                                  contact_phone=phone,
                                  )
                    order.save()
                    data = {'username': order.username, 'order': order}
                    return render(request, 'order_app/order_notes2.html', data)
                except Exception as e:
                    return HttpResponse('There is no that item in the basket',e)

    pressed = ''
    try:
        pressed = request.get_full_path()
        pressed = pressed.split('add')
        pressed = int(pressed[-1])
    except Exception as e:
        print('EXCEPTION ---', e)

    u = request.user
    delete_not_accept_orders(u) # cleaning not ending orders
    if type(pressed) == int:  #view items in basket
        if u.is_authenticated:
            if u.is_active:
                item = Basket.objects.get(id=pressed)
                OrderNotes.item = item
                OrderNotes.item_id = pressed
                data = {'username': u.username, 'item': item,}
                return render(request, 'order_app/order_notes.html', data)
    return HttpResponse('Проблема с авторизацией')


def delete_order(request):
    u = request.user
    try:
        order_to_delete = request.get_full_path()
        order_to_delete = order_to_delete.split('?')
        order_to_delete = int(order_to_delete[-1])
        order = Order.objects.get(id=order_to_delete)
        order.delete()
    except Exception as e:
        print('EXCEPTION ---', e)

    order_id = []
    orders = []

    for i in Basket.objects.filter(username=u.username):
        order_id.append(i.pk)

    for i in order_id:
        o = Basket.objects.get(pk=i)
        orders.append(o)

    data = {'username': u.username, 'orders': orders}

    return render(request, 'order_app/basket.html', data)


def submit_order(request):
    u = request.user
    data = {'username': u.username}
    pay_method = ''
    this_order = ''
    try:
        pay_method = request.get_full_path()
        pay_method = pay_method.split('?')
        pay_method = pay_method[-1]
    except Exception as e:
        print('EXCEPTION ---', e)

    for i in Order.objects.filter(username=u.username):
        if i.is_accept == False:
            if i.add_information == '':
                this_order = i
    if this_order == '':
        return HttpResponse('Request Error')

    if pay_method == 'paylater':
        this_order.date_created = timezone.now() # update order and finish
        this_order.is_accept = True
        this_order.add_information = 'check order data and approve order or contact with order person'

        delete_from_basket(u, this_order) # delete ordered thing from user basket
        update_storage(this_order.order_item_name, this_order.order_item_size)

        this_order.save()

        return render(request, 'order_app/finish_order.html', data)

    if pay_method == 'paynow':
        if this_order.sum_price > u.money:
            data = {'username': this_order.username, 'order': this_order, 'money_error': 'not enough money' }
            return render(request, 'order_app/order_notes2.html', data)
        else:
            this_order.date_created = timezone.now()  # update order and finish
            this_order.is_accept = True
            this_order.add_information = 'check order data and approve order or contact with order person'

            delete_from_basket(u, this_order)  # delete ordered thing from user basket
            update_storage(this_order.order_item_name, this_order.order_item_size)
            u.money = u.money - this_order.sum_price
            u.save()
            this_order.is_paid = True
            this_order.save()

            return render(request, 'order_app/finish_order.html', data)


def make_order_all(request):
    if request.method == 'POST':
        u = request.user
        if u.is_authenticated:
            if u.is_active:
                for i in Basket.objects.filter(username=u.username):
                    country = request.POST.get('country')
                    city = request.POST.get('city')
                    street = request.POST.get('street')
                    house = request.POST.get('house')
                    postcode = request.POST.get('postcode')
                    phone = request.POST.get('phone')
                    errors = valid_data_from_user(country, city, street, house, postcode, phone)  # check user data
                    if len(errors) > 0:
                        data = {'username': u.username, 'items': OrderNotes.items_order_all,
                                'price_all': OrderNotes.price_all, 'errors': errors}
                        return render(request, 'order_app/order_notes.html', data)
                    try:
                        print('OrderNotes.item_id  --- ', OrderNotes.item_id)
                        items, sizes, prices, sum_prices = ['', '', '', 0]

                        for i in Basket.objects.filter(username=u.username):
                            basket_item = i
                            basket_item.mark = 'to delete'
                            basket_item.save()
                            items += i.item_name + '*' + i.item_size + ', '
                            sizes = 'watch item name column'
                            prices += str(i.item_price) + ' + '
                            sum_prices += i.item_price

                        order = Order(username=u.username,
                                      order_item_name=items,
                                      order_item_size=sizes,
                                      items_price=prices,
                                      sum_price=sum_prices,
                                      ship_country=country,
                                      ship_city=city,
                                      ship_street=street,
                                      ship_house=house,
                                      ship_postalcode=postcode,
                                      contact_phone=phone,
                                      )
                        order.save()
                        data = {'username': order.username, 'order': order}
                        return render(request, 'order_app/order_notes2.html', data)
                    except Exception as e:
                        return HttpResponse('There is no that item in the basket', e)
        return HttpResponse('Post Order all mistake')

    u = request.user
    delete_not_accept_orders(u) # cleaning not ending orders
    if u.is_authenticated:
        if u.is_active:
            items = []
            price_all = 0
            for i in Basket.objects.filter(username=u.username):
                items.append(i)
                price_all += i.item_price
            OrderNotes.items_order_all = items
            OrderNotes.price_all = price_all
            data = {'username': u.username, 'items': items, 'price_all': price_all}
            return render(request, 'order_app/order_notes.html', data)
    return HttpResponse('GET Order all mistake')



