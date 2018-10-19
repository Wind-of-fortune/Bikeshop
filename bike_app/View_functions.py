from django.contrib.auth import get_user

from bike_app.models import MountBikes


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

def size_filter_mountbike(size):
    querylist = MountBikes.objects.filter(bike_type='mountbike')
    bikes = []

    if size == 'xs':
        for i in querylist:
            if i.available_XS > 0:
                bikes.append(i)
        return bikes

    if size == 'ss':
        for i in querylist:
            if i.available_S > 0:
                bikes.append(i)
        return bikes

    if size == 'mm':
        for i in querylist:
            if i.available_M > 0:
                bikes.append(i)
        return bikes

    if size == 'll':
        for i in querylist:
            if i.available_L > 0:
                bikes.append(i)
        return bikes

    if size == 'xl':
        for i in querylist:
            if i.available_XL > 0:
                bikes.append(i)
        return bikes

def size_filter_roadbike(size):
    querylist = MountBikes.objects.filter(bike_type='roadbike')
    bikes = []

    if size == 'xs':
        for i in querylist:
            if i.available_XS > 0:
                bikes.append(i)
        return bikes

    if size == 'ss':
        for i in querylist:
            if i.available_S > 0:
                bikes.append(i)
        return bikes

    if size == 'mm':
        for i in querylist:
            if i.available_M > 0:
                bikes.append(i)
        return bikes

    if size == 'll':
        for i in querylist:
            if i.available_L > 0:
                bikes.append(i)
        return bikes

    if size == 'xl':
        for i in querylist:
            if i.available_XL > 0:
                bikes.append(i)
        return bikes


def price_min_max(querylist, price_min, price_max):
    bikes = []
    for i in querylist:
        if price_min <= i.price <= price_max:
            bikes.append(i)
    return bikes


# Функция - костыль для парсинга url и взятия из него нужных параметров
def get_bike_name_and_last_page_url(mountbike_path, mountbike_uri):
    bike_name = None

    if mountbike_path.find('mountbike'):
        bike_name = mountbike_path.replace('/bike/mountbike/name/?', '')

    if mountbike_path.find('roadbike'):
        bike_name = mountbike_path.replace('/bike/roadbike/name/?', '')

    if mountbike_path.find('bmxbike'):
        bike_name = mountbike_path.replace('/bike/bmxbike/name/?', '')

    bike_string = bike_name.split('*')
    bike_name = bike_string[1]
    bike_name = bike_name.replace('%20', ' ')

    mountbike_name = mountbike_uri.split('*')
    mountbike_name = mountbike_name[0]
    a = mountbike_name.split('name/')
    b = a[0]
    c = a[1]
    mountbike_uri = b + c

    return bike_name, mountbike_uri


# deleted AnonymousUser from templates
def delete_anonim (request):
    if str(get_user(request)) == 'AnonymousUser':
        return None
    else:
        return get_user(request)


def size_string(this_bike):
    new_sizes = ''
    if this_bike.mountbikes.available_XS > 0:
        new_sizes += '  XS'
    if this_bike.mountbikes.available_S > 0:
        new_sizes += '  S'
    if this_bike.mountbikes.available_M > 0:
        new_sizes += '  M'
    if this_bike.mountbikes.available_L > 0:
        new_sizes += '  L'
    if this_bike.mountbikes.available_XL > 0:
        new_sizes += '  XL'
    if new_sizes == '':
        new_sizes = 'Товара нет в наличии'

    return new_sizes

def size_list(new_sizes):
    size_list = []
    if new_sizes != 'Товара нет в наличии':
        sl = new_sizes.split(' ')
        for i in range(len(sl)):
            if sl[i] != '':
                size_list.append(sl[i])

    return size_list


def menu_filter_size_mountbike (size):
    if size == 'xs' or size == 'ss' or size == 'mm' or size == 'll' or size == 'xl':
        bikes = size_filter_mountbike(size)
        return bikes


def ident_bike_type(path):
    if path.find('mountbike') != -1:
        return 'mountbike'
    if path.find('roadbike') != -1:
        return 'roadbike'
    if path.find('bmx') != -1:
        return 'bmx'
    if path.find('citybike') != -1:
        return 'city_bike'
    if path.find('kidsbike') != -1:
        return 'child_bike'
