string = '/bike/mountbike/name/?zaskar%20comp%202018/'

new_string = '/bike/mountbike/name/?'

string = string.replace('/bike/mountbike/name/?', '')
string = string.replace('/', '')
string = string.replace('%20', ' ')

print(string)


def mountbike_model(request):
    if request.GET.get('bike_name') != None:
        # mountbike_name = request.get_full_path()
        # bike_name = mountbike_name.replace('/bike/mountbike/name/?', '')
        # bike_name = bike_name.replace('/', '')
        # bike_name = bike_name.replace('%20', ' ')
        bike_name = request.GET.get('bike_name')
        previous_page = request.GET.get('previous_page')
        new_page = request.get_raw_uri()

        print('bike_name is ---- ', bike_name)
        print('previous_page is ---- ', previous_page)

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
                        'previous_page': previous_page,
                        'new_page': new_page,
                        }
                return render(request, 'bike_app/mountbike_id.html', data)

    return HttpResponse('Something goes wrong')









