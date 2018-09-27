
from django.shortcuts import render
from bike_app.models import *

from bike_app.View_functions import *


def main_page(request):
    return render(request, 'bike_app/main_page.html')


def mountbike(request):
    bikes = bike_sort_by_repeats(MountBikes.objects.all())

    available = request.GET.get('available')
    price = request.GET.get('price')
    size = request.GET.get('size')
    brand = request.GET.get('brand')
    price_min = request.GET.get('pricemin')
    price_max = request.GET.get('pricemax')
    print('PRAICE_MIN IS -----', price_min)

    if available == 'true':
        old_bikes = bikes
        bikes = []

        for i in old_bikes:  # sort by available
            if i.available == True:
                bikes.append(i)

    if price == 'true':
        bikes = price_low_filter(bikes)

    if price == 'false':
        bikes = price_high_filter(bikes)

    if brand == 'true':
        bikes = brand_filter(bikes)

    if size == 'xs' or size == 's' or size == 'm' or size == 'l' or size == 'xl':
        bikes = size_filter(size)

    if price_min != 'null' or price_min != None and price_max != 'null' or price_max != None:
        try:
            print('TYPE OF  ------', type(price_min), type(price_max))
            price_min = int(price_min)
            price_max = int(price_max)
            bikes = price_min_max(bikes, price_min, price_max)
        except Exception as err:
            print('EEERRROOORRR  ---- ',err)

    table_column = check_1_or_0(bikes)
    bikes_1, bikes_2 = two_bikes_lists(bikes)

    return render(request, 'bike_app/mountbike_page.html', {'bikes': bikes,
                                                            'bikes_1': bikes_1,
                                                            'bikes_2': bikes_2,
                                                            'table_column': table_column,
                                                            'available1': available,
                                                            'price1': price,
                                                            'size1': size,
                                                            'brand1': brand,
                                                            })

#
#
# def mountbike_sort_by_available(request):
#     bikes = bike_sort_by_repeats(MountBikes.objects.all())
#
#     old_bikes = bikes
#     bikes = []
#     for i in old_bikes:             # sort by available
#         if i.available == True:
#             bikes.append(i)
#
#     table_column = check_1_or_0(bikes)
#     bikes_1, bikes_2 = two_bikes_lists(bikes)
#
#     return render(request, 'bike_app/mountbike_page.html', {'bikes': bikes,
#                                                             'bikes_1': bikes_1,
#                                                             'bikes_2': bikes_2,
#                                                             'table_column': table_column,
#                                                             })
#
#
# def mountbike_sort_by_price_low_to_high(request):
#     b = bike_sort_by_repeats(MountBikes.objects.all())
#
#     bikes = price_func(b)
#
#     table_column = check_1_or_0(bikes)
#     bikes_1, bikes_2 = two_bikes_lists(bikes)
#
#     return render(request, 'bike_app/mountbike_page.html', {'bikes': bikes,
#                                                             'bikes_1': bikes_1,
#                                                             'bikes_2': bikes_2,
#                                                             'table_column': table_column,
#                                                             })
#
#
# def mountbike_sort_by_price_high_to_low(request):
#     b = bike_sort_by_repeats(MountBikes.objects.all())
#
#     bikes = price_func(b)
#     bikes.reverse()
#
#     table_column = check_1_or_0(bikes)
#     bikes_1, bikes_2 = two_bikes_lists(bikes)
#
#     return render(request, 'bike_app/mountbike_page.html', {'bikes': bikes,
#                                                              'bikes_1': bikes_1,
#                                                              'bikes_2': bikes_2,
#                                                              'table_column': table_column,
#                                                              })
#
# def mountbike_sort_by_brand(request):
#     b = bike_sort_by_repeats(MountBikes.objects.all())
#
#     bikes = brand_func(b)
#
#     table_column = check_1_or_0(bikes)
#     bikes_1, bikes_2 = two_bikes_lists(bikes)
#
#     return render(request, 'bike_app/mountbike_page.html', {'bikes': bikes,
#                                                             'bikes_1': bikes_1,
#                                                             'bikes_2': bikes_2,
#                                                             'table_column': table_column,
#                                                             })

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
