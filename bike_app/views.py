from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import get_user

from bike_app.models import *
from bike_app.View_functions import *
from order_app.models import Basket


def main_page(request):
    username = delete_anonim(request)
    return render(request, 'bike_app/main_page.html', {'username': username})


def mountbike(request):
    username = delete_anonim(request)

    bikes = MountBikes.objects.all()
    filtered_by_size_bikes = False

    available = request.GET.get('available')
    discount = request.GET.get('discount')
    price = request.GET.get('price')
    size = request.GET.get('size')
    brand = request.GET.get('brand')
    price_min = request.GET.get('pricemin')
    price_max = request.GET.get('pricemax')

    if size == 'xs' or size == 'ss' or size == 'mm' or size == 'll' or size == 'xl':
        bikes = size_filter(size)
        filtered_by_size_bikes = bikes

    if price == 'low':
        if filtered_by_size_bikes != False:
            bikes = filtered_by_size_bikes
        bikes = price_low_filter(bikes)

    if price == 'high':
        if filtered_by_size_bikes != False:
            bikes = filtered_by_size_bikes
        bikes = price_high_filter(bikes)

    if brand == 'true':
        if filtered_by_size_bikes != False:
            bikes = filtered_by_size_bikes
        bikes = brand_filter(bikes)


    if available == 'true':
        if filtered_by_size_bikes != False:
            old_bikes = filtered_by_size_bikes
            bikes = []
        else:
            old_bikes = bikes
            bikes = []

        for i in old_bikes:  # sort by available
            if i.available_XS > 0:
                bikes.append(i)
                continue
            if i.available_S > 0:
                bikes.append(i)
                continue
            if i.available_M > 0:
                bikes.append(i)
                continue
            if i.available_L > 0:
                bikes.append(i)
                continue
            if i.available_XL > 0:
                bikes.append(i)
                continue


    if discount == 'true':
        if filtered_by_size_bikes != False:
            old_bikes = filtered_by_size_bikes
            bikes = []
        else:
            old_bikes = bikes
            bikes = []

        for i in old_bikes:  # sort by discount
            if i.discount > 0:
                bikes.append(i)


    if price_min != '' or price_min != None and price_max != '' or price_max != None:
        try:
            price_min = int(price_min)
            price_max = int(price_max)
            bikes = price_min_max(bikes, price_min, price_max)
        except Exception as err:
            pass
            #print('EEERRROOORRR  ---- ',err)

    table_column = check_1_or_0(bikes)
    bikes_1, bikes_2 = two_bikes_lists(bikes)

    data = {'bikes': bikes,
            'bikes_1': bikes_1,
            'bikes_2': bikes_2,
            'table_column': table_column,
            'available1': available,
            'discount': discount,
            'price1': price,
            'size1': size,
            'brand1': brand,
            'pricemin': price_min,
            'pricemax': price_max,
            'username': username,
            }

    return render(request, 'bike_app/mountbike_page.html', data )

class BasketState:
    name = ''
    price=''

def mountbike_model(request):
    if request.method == 'POST':
        u = request.user
        if u.is_authenticated:
            if u.is_active:
                basket_item_xs = request.POST.get('XS')
                basket_item_s = request.POST.get('S')
                basket_item_m = request.POST.get('M')
                basket_item_l = request.POST.get('L')
                basket_item_xl = request.POST.get('XL')
                s = [basket_item_xs, basket_item_s, basket_item_m, basket_item_l, basket_item_xl]
                size=''
                for i in range(len(s)):
                    if s[i] != None:
                        size = s[i]
                if size == '':
                    return render(request, 'order_app/basket_add.html', {'miss': 'Такого товара нет'})

                new_order = Basket(item_name=BasketState.name,
                                   item_price=BasketState.price,
                                   item_size= size,
                                   username= u.username,
                                   date_created=timezone.now(),
                                   )
                new_order.save()

                data = {'id': u.pk,
                        'username': u.username,
                        'first_name': u.first_name,
                        'last_name': u.last_name,
                        'email': u.email,
                        'money': u.money,
                        'item_name': BasketState.name,
                        'item_size': size,
                        'item_price': BasketState.price
                        }


                return render(request, 'order_app/basket_add.html', data)
            else:
                return HttpResponse('Поздравляем вас добавили в игнор лист, вам запрещено у нас что-либо покупать')


    username = delete_anonim(request)

    bike_name, mountbike_url = get_bike_name_and_last_page_url(request.get_full_path(), request.get_raw_uri())

    for name in MountBikesDescription.objects.all():
        if name.mountbikes.name == bike_name:
            this_bike = name

            new_sizes = size_string(this_bike)
            size_l = size_list(new_sizes)

            print('SIZE LIST --- ', size_l)

            if this_bike.unisex == True:
                sex = 'Унисекс'
            else:
                sex = 'Женский'

            data = {'name': this_bike.mountbikes.name,
                    'description': this_bike.description,
                    'sex': sex,
                    'year': this_bike.mountbikes.year,
                    'frame': this_bike.frame,
                    'fork': this_bike.fork,
                    'crank': this_bike.crank,
                    'wheels': this_bike.wheels,
                    'front_shifter': this_bike.front_shifter,
                    'rear_shifter': this_bike.rear_shifter,
                    'front_brake': this_bike.front_brake,
                    'rear_brake': this_bike.rear_brake,
                    'handlebar': this_bike.handlebar,
                    'seat': this_bike.seat,
                    'warranty': this_bike.warranty,
                    'size': new_sizes,
                    'size_list': size_l,
                    'price': this_bike.mountbikes.price,
                    'brand': this_bike.mountbikes.brand,
                    'img_link': this_bike.mountbikes.img_link,
                    'go_back': mountbike_url,
                    'username': username,
                }
            BasketState.name = this_bike.mountbikes.name
            BasketState.price = this_bike.mountbikes.price

            return render(request, 'bike_app/mountbike_id.html', data)

    return HttpResponse('Something goes wrong')


    # JSON
# def mountbike_dynamic(request):         # all objects without any sort
#     bikes = bike_sort_by_repeats(MountBikes.objects.all())
#     new_bikes = []
#     id_bikes = []
#     new_dict = {}
#     for bike in bikes:
#         new_bikes.append(MountBikes.to_dict(bike))
#         id_bikes.append(bike.id)
#     new_dict = dict(zip(id_bikes, new_bikes))
#     print(new_dict)
#     return JsonResponse(new_dict)
