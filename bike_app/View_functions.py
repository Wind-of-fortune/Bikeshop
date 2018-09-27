from bike_app.models import MountBikes
import re

def bike_sort_by_repeats(querylist):
    a = list(querylist)
    bikes_set = []
    bikes = []

    for i in a:  # создаем новый лист без повторяющихся имен
        bikes_set.append(str(i))
    bikes_set = set(bikes_set)

    new_dict = dict(zip(bikes_set, querylist))

    for k in sorted(new_dict.keys()):
        bikes.append(new_dict[k])
    return bikes


def check_1_or_0(querylist):
    if querylist.__len__() % 2 == 0:
        table_column = 0
    else:
        table_column = 1

    return table_column


def two_bikes_lists(querylist):
    bikes = querylist
    bikes_1 = []
    bikes_2 = []

    k = -1
    for i in bikes:
        k += 1
        if k % 2 == 0:
            bikes_1.append(i)
        else:
            bikes_2.append(i)

    return bikes_1, bikes_2


def price_low_filter(querylist):
    price_var = []
    bikes = []
    count = 0

    for i in querylist:
        count += 1
        price_var.append(i.price + count)
    new_dict = dict(zip(price_var, querylist))

    for k in sorted(new_dict.keys()):
        bikes.append(new_dict[k])

    return bikes


def price_high_filter(querylist):
    price_var = []
    bikes = []
    count = 0

    for i in querylist:
        count += 1
        price_var.append(i.price + count)
    new_dict = dict(zip(price_var, querylist))

    for k in sorted(new_dict.keys(), reverse=True):
        bikes.append(new_dict[k])

    return bikes



def brand_filter(querylist):
    brand_var = []
    bikes = []
    count = 0
    for i in querylist:
        count += 1
        brand_var.append(i.brand + str(count))
    new_dict = dict(zip(brand_var, querylist))

    for k in sorted(new_dict.keys()):
        bikes.append(new_dict[k])

    return bikes

def size_filter(size):
    querylist = MountBikes.objects.all()
    bikes = []
    print('QUERY  - ', querylist)
    for i in querylist:
        if i.size == str(size.upper()):
            bikes.append(i)
    print('SIZE  - ', bikes)
    return bikes


def price_min_max(querylist, price_min, price_max):
    bikes = []
    for i in querylist:
        if price_min <= i.price <= price_max:
            bikes.append(i)
    return bikes

