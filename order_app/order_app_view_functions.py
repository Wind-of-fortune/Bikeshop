
from order_app.models import *

def delete_not_accept_orders(user):
    if user.is_authenticated:
        if user.is_active:
            delete_not_accept = []
            for i in Order.objects.all():
                if i.username == user.username:
                    if i.is_accept == False:
                        delete_not_accept.append(i.pk)
            for i in delete_not_accept:
                o = Order.objects.get(id=i)
                o.delete()


def delete_from_basket(user, order): # delete ordered thing from user basket
    basket_item_to_delete = ''
    k = order.order_item_name.find('*')
    if k != -1:
        print('order.order_item_name', order.order_item_name)
        iter = 0
        for i in Basket.objects.all():
            if i.username == user.username:
                iter += 1

        for j in range(iter):
            for i in Basket.objects.all():
                if i.username == user.username:
                    basket_item_to_delete = i
            basket_item_to_delete.delete()
    else:
        for i in Basket.objects.all():
            if i.username == user.username:
                if i.mark == 'to_delete':
                    basket_item_to_delete = i
        basket_item_to_delete.delete()


def delete_all_todelete_from_basket(user): # delete all  marks 'to_delete'
    for i in Basket.objects.all():
        if i.username == user.username:
            if i.mark == 'to_delete':
                k = i
                k.mark = ''
                k.save()

def update_storage_dop(name, size):

    b = MountBikes.objects.get(name=name)

    if size == 'XS':
        b.available_XS = b.available_XS -1
        b.save()

    if size == 'S':
        b.available_S = b.available_S -1
        b.save()

    if size == 'M':
        b.available_M = b.available_M -1
        b.save()

    if size == 'L':
        b.available_L = b.available_L -1
        b.save()

    if size == 'XL':
        b.available_XL = b.available_XL -1
        b.save()

def update_storage(name, size): # update storage after ordering
    if size == 'watch item name column':
        a = name.split(',')
        bikes = []
        sizes = []
        try:
            for i in a:
                k = i.split('*')
                bikes.append(k[0].strip())
                sizes.append(k[1])
        except Exception:
            pass
        bikes.pop(-1)
        print(bikes)
        print(sizes)
        for i in range(len(bikes)):
            update_storage_dop(bikes[i],sizes[i])
    else:
        update_storage_dop(name,size)


def valid_data_from_user(country,city,street,house,postcode,phone):
    error_list = []
    country_list = ['Россия','Белоруссия','Украина']
    k = 0

    if country == '':
        error_list.append('Извините, но "Страна" необходимое для ввода поле')
    if city == '':
        error_list.append('Извините, но "Город" необходимое для ввода поле')
    if street == '':
        error_list.append('Извините, но "Улица" необходимое для ввода поле')
    if house == '':
        error_list.append('Извините, но "Дом" необходимое для ввода поле')
    if postcode == '':
        error_list.append('Извините, но "Почтовый код" необходимое для ввода поле')
    if phone == '':
        error_list.append('Извините, но "Ваш контактный телефон" необходимое для ввода поле')

    for i in country_list:
        if country == i:
            k+=1
    if k == 0:
        error_list.append('Извините, но мы достаялем нашы товары пока только в эти страны -  '
                          'Россия, Белоруссия, Украина'
                          '')
    try:
        p = int(postcode)
    except Exception as e:
        error_list.append('Проверьте ваш почтовый код, вы ошиблись')

    try:
        p = int(phone)
    except Exception as e:
        error_list.append('Проверьте ваш контактный телефон, вы ошиблись')

    return error_list

