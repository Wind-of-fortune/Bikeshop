



def bmxbike_model(request):
    if request.method == 'POST':
        u = request.user
        if u.is_authenticated:
            if u.is_active:
                new_order = Basket(item_name=BasketState.name,
                                   item_price=BasketState.price,
                                   username= u.username,
                                   )
                new_order.save()

                data = {'id': u.pk,
                        'username': u.username,
                        'first_name': u.first_name,
                        'last_name': u.last_name,
                        'email': u.email,
                        'money': u.money,
                        'item_name': BasketState.name,
                        'item_price': BasketState.price
                        }

                return render(request, 'order_app/basket_add.html', data)
            else:
                return HttpResponse('Поздравляем вас добавили в игнор лист, вам запрещено у нас что-либо покупать')

    username = delete_anonim(request)
    bike_name, mountbike_url = get_bike_name_and_last_page_url(request.get_full_path(), request.get_raw_uri())
    this_bike = BMXBikesDescription.objects.get(mountbikes=bike_name)

    data = {'name': this_bike.mountbikes.name,
            'description': this_bike.description,
            'year': this_bike.mountbikes.year,
            'frame': this_bike.frame,
            'fork': this_bike.fork,
            'crank': this_bike.crank,
            'wheels': this_bike.wheels,
            'handlebar': this_bike.handlebar,
            'seat': this_bike.seat,
            'warranty': this_bike.warranty,
            'price': this_bike.mountbikes.price,
            'brand': this_bike.mountbikes.brand,
            'img_link': this_bike.mountbikes.img_link,
            'go_back': mountbike_url,
            'username': username,
            'type': this_bike.mountbikes.bike_type,
            'available_no_size': this_bike.mountbikes.available_no_size
        }
    BasketState.name = this_bike.mountbikes.name
    BasketState.price = this_bike.mountbikes.price

    return render(request, 'bike_app/mountbike_id.html', data)


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

            'price': this_bike.mountbikes.price,
            'brand': this_bike.mountbikes.brand,
            'img_link': this_bike.mountbikes.img_link,
            'go_back': mountbike_url,
            'username': username,

            'this_bike':this_bike,
            'size': new_sizes,
            'size_list': size_l,
            'type': this_bike.mountbikes.bike_type
        }



    def mountbike(request):
        username = delete_anonim(request)

        bikes = MountBikes.objects.filter(bike_type='mountbike')
        filtered_by_size_bikes = False

        available = request.GET.get('available')
        discount = request.GET.get('discount')
        price = request.GET.get('price')
        size = request.GET.get('size')
        brand = request.GET.get('brand')
        price_min = request.GET.get('pricemin')
        price_max = request.GET.get('pricemax')

        if size == 'xs' or size == 'ss' or size == 'mm' or size == 'll' or size == 'xl':
            bikes = size_filter_mountbike(size)
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
                if i.fake_price != i.price > 0:
                    bikes.append(i)

        if price_min != '' or price_min != None and price_max != '' or price_max != None:
            try:
                price_min = int(price_min)
                price_max = int(price_max)
                bikes = price_min_max(bikes, price_min, price_max)
            except Exception as err:
                pass
                # print('EEERRROOORRR  ---- ',err)

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

        return render(request, 'bike_app/mountbike_page.html', data)





    data = {'bikes': bikes,
            'bikes_1': bikes_1,
            'bikes_2': bikes_2,
            'table_column': table_column,
            'available1': available,
            'discount': discount,
            'price1': price,
            'brand1': brand,
            'pricemin': price_min,
            'pricemax': price_max,
            'username': username,
            }

    if biketype == 'mountbike' or biketype == 'roadbike':
        data['size1']: size

    return render(request, 'bike_app/mountbike_page.html', data)
