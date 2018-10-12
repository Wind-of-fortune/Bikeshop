
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


def delete_from_basket(user): # delete ordered thing from user basket
    basket_item_to_delete = ''
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

def update_storage(name, size): # update storage after ordering
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
