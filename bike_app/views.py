import re

from django.shortcuts import render
from bike_app.models import *
from django.http import HttpResponse, JsonResponse

from bike_app.View_functions import *


def main_page(request):
    return render(request, 'bike_app/main_page.html')


def mountbike(request):
    bikes = MountBikes.objects.all()

    available = request.GET.get('available')
    price = request.GET.get('price')
    size = request.GET.get('size')
    brand = request.GET.get('brand')
    price_min = request.GET.get('pricemin')
    price_max = request.GET.get('pricemax')

    if available == 'true':
        old_bikes = bikes
        bikes = []

        for i in old_bikes:  # sort by available
            if i.available == True:
                bikes.append(i)

    if price == 'low':
        bikes = price_low_filter(bikes)

    if price == 'high':
        bikes = price_high_filter(bikes)

    if brand == 'true':
        bikes = brand_filter(bikes)

    if size == 'xs' or size == 'ss' or size == 'mm' or size == 'll' or size == 'xl':
        bikes = size_filter(size)

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
            'price1': price,
            'size1': size,
            'brand1': brand,
            'pricemin': price_min,
            'pricemax': price_max,
            }

    return render(request, 'bike_app/mountbike_page.html', data )


def mountbike_model(request):

    bike_name, mountbike_url = get_bike_name_and_last_page_url(request.get_full_path(), request.get_raw_uri())

    for name in MountBikesDescription.objects.all():
        if name.mountbikes.name == bike_name:
            this_bike = name
            data = {'name': this_bike.mountbikes.name,
                    'description': this_bike.description,
                    'sex': this_bike.sex,
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
                    'size': this_bike.mountbikes.size,
                    'price': this_bike.mountbikes.price,
                    'brand': this_bike.mountbikes.brand,
                    'available': this_bike.mountbikes.available,
                    'img_link': this_bike.mountbikes.img_link,
                    'go_back': mountbike_url,
                }
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
