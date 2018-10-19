
import random
import os

import requests
from bs4 import BeautifulSoup

from django.db import transaction

from bike_app.models import *

#'https://trial-sport.ru/goods/51516/1320481.html'
def get_data_mountbike(url_path):
    url = 'https://trial-sport.ru' + url_path
    r = requests.get(url)
    soup = BeautifulSoup(r.content)

    title = soup.h2.get_text()

    k = soup.find_all("div", {"class":"ai_sub_c"})
    t = []
    for i in k:
        t.append(i.get_text())

    #----------------------# # get price and discount price
    our_data = str(t[0])

    our_data = our_data.split('Бренд:')
    description = our_data[0]
    our_data = our_data[1]

    our_data = our_data.split('Цена:')
    our_data = our_data[1]
    our_data = our_data.split('Цена')
    price = our_data[0]
    our_data = our_data[1]

    our_data = our_data.split('по акции:')
    price_discount = our_data[1]

    new_price = ''
    new_discount_price = ''

    for i in price:
        if i.isdigit():
            new_price += i

    for i in price_discount:
        if i.isdigit():
            new_discount_price += i

    price = int(new_price)
    price_discount = int(new_discount_price)
    #----------------------#

    #----------------------#   # get all except price, image, size, title
    k1 = soup.find_all("tr", {"class":"border"})
    new_list =[]
    e1=[]
    e2=[]
    for i in k1:
        new_list.append(i.get_text())

    for i in new_list:
        rrr=i.split(':')
        e1.append(rrr[0])
        e2.append(rrr[1])
    new_dict = dict(zip(e1,e2))

    #----------------------#

    #----------------------# # get image link
    try:
        image = soup.find("div", {"data-id":"img0"})
        yy = str(image)
        yy = yy.split('url(')
        yy = yy[1]
        yy = yy.split(')"')
        yy = yy[0]
        yy = yy.replace('200/','')
        image = 'https://trial-sport.ru' + yy

        f = open(r'C:\python_projects\BikeShop\bike_app\static\bike_app\bike_models\Mountbikes'
                 + r'\\' + title + ' ' +  new_dict['Год'] + '.' + 'jpg', 'wb')
        f.write(requests.get(image).content)
        f.close()
    except Exception:
        try:
            image = soup.find("div", {"data-id": "color0"})
            yy = str(image)
            yy = yy.split('url(')
            yy = yy[1]
            yy = yy.split(')"')
            yy = yy[0]
            yy = yy.replace('200/', '')
            image = 'https://trial-sport.ru' + yy

            f = open(r'C:\python_projects\BikeShop\bike_app\static\bike_app\bike_models\Mountbikes'
                     + r'\\' + title + ' ' + new_dict['Год'] + '.' + 'jpg', 'wb')
            f.write(requests.get(image).content)
            f.close()
        except Exception:
            image = 2
            print("IMAGE----ERROR")
    #----------------------# get size
    try:
        size = new_dict['Поставляемые размеры']

        if size.find('XS') != -1:
            available_xs = random.randint(1, 10)
        else:
            available_xs = 0

        if size.find('S') != -1:
            available_s = random.randint(1, 10)
        else:
            available_s = 0

        if size.find('M') != -1:
            available_m = random.randint(1, 10)
        else:
            available_m = 0

        if size.find('L') != -1:
            available_l = random.randint(1, 10)
        else:
            available_l = 0

        if size.find('XL') != -1:
            available_xl = random.randint(1, 10)
        else:
            available_xl = 0

    except Exception:
        available_xs = random.randint(1, 10)
        available_s = random.randint(1, 10)
        available_m = random.randint(1, 10)
        available_l = random.randint(1, 10)
        available_xl = random.randint(1, 10)


    #----------------------# # Mountbike data
    name = title + ' ' +  new_dict['Год']
    brand = new_dict['Бренд']
    year = int(new_dict['Год'])
    fake_price = price
    price = price_discount
    img_link = name + '.jpg'
    bike_type = 'mountbike'
    #----------------------# # MountbikeDescription data
    description = description
    frame = new_dict['Рама']
    fork = new_dict['Вилка']

    try:
        ammort = new_dict['Задний амортизатор']
    except Exception:
        ammort = 'отсутствует'

    try:
        crank = new_dict['Система']
    except Exception:
        try:
            crank = new_dict['Шатуны']
        except Exception:
            crank = 'отсутствует'

    try:
        pedal = new_dict['Педали']
    except Exception:
        pedal = 'отсутствуют'
    try:
        front_shifter = new_dict['Передний переключатель']
    except Exception:
        front_shifter = 'отсутствует'
    try:
        rear_shifter = new_dict['Задний переключатель']
    except Exception:
        rear_shifter = 'отсутствует'
    try:
        lever = new_dict['Манетки']
    except Exception:
        lever = 'отсутствуют'
    try:
        cassete = new_dict['Кассета']
    except Exception:
        cassete = 'отсутствует'
    try:
        chain = new_dict['Цепь']
    except Exception:
        chain = 'нет'
    try:
        rims = new_dict['Обода']
    except Exception:
        rims = 'нет'
    try:
        tyres = new_dict['Покрышки']
    except Exception:
        tyres = 'нет'
    try:
        front_hub = new_dict['Передняя втулка']
    except Exception:
        front_hub = 'нет'
    try:
        rear_hub = new_dict['Задняя втулка']
    except Exception:
        rear_hub = 'нет'
    try:
        front_brake = new_dict['Передний тормоз']
    except Exception:
        front_brake = 'отсутствует'
    try:
        rear_brake = new_dict['Задний тормоз']
    except Exception:
        rear_brake = 'отсутствует'
    try:
        handlebar = new_dict['Руль']
    except Exception:
        handlebar = 'нет'
    try:
        stem = new_dict['Вынос руля']
    except Exception:
        stem = 'нет'
    try:
        grips = new_dict['Грипсы']
    except Exception:
        grips = 'нет'
    try:
        headset = new_dict['Рулевая колонка']
    except Exception:
        headset = 'нет'
    try:
        saddle = new_dict['Седло']
    except Exception:
        saddle = 'отсутствует'
    try:
        seatpost = new_dict['Подседельный штырь']
    except Exception:
        seatpost = 'отсутствует'

    try:
        print(price, price_discount)
        try:
            MountBikes.objects.get(name=name)
            print('Name Repeat! -- ', name)
            os.remove(r'C:\python_projects\BikeShop\bike_app\static\bike_app\bike_models\Mountbikes'
                      + r'\\' + title + ' ' + new_dict['Год'] + '.' + 'jpg')
        except:

            if image == 2:
                print('NO IMAGE -- ', image)

            else:
                bike = MountBikes(name=name, brand=brand, year=year, fake_price=fake_price, price=price,
                                  img_link=img_link, bike_type=bike_type, available_XS=available_xs,
                                  available_S=available_s, available_M=available_m, available_L=available_l,
                                  available_XL=available_xl)

                bikedescription = MountBikesDescription(mountbikes=bike, description=description, frame=frame, ammort=ammort,
                                                        fork=fork, crank=crank, pedal=pedal, front_shifter=front_shifter,
                                                        rear_shifter=rear_shifter, lever=lever, cassete=cassete, chain=chain,
                                                        rims=rims, tyres=tyres, front_hub=front_hub, rear_hub=rear_hub,
                                                        front_brake=front_brake, rear_brake=rear_brake, handlebar=handlebar,
                                                        stem=stem, grips=grips, headset=headset, saddle=saddle, seatpost=seatpost)

                bike.save()
                bikedescription.save()
    except Exception:
        print('BIKE----SAVE EXCEPTION')
        os.remove(r'C:\python_projects\BikeShop\bike_app\static\bike_app\bike_models\Mountbikes'
                 + r'\\' + title + ' ' + new_dict['Год'] + '.' + 'jpg')

################## Kids bikes #########################

def get_data_kids(url_path):
    url = 'https://trial-sport.ru' + url_path
    r = requests.get(url)
    soup = BeautifulSoup(r.content)

    title = soup.h2.get_text()

    k = soup.find_all("div", {"class":"ai_sub_c"})
    t = []
    for i in k:
        t.append(i.get_text())

    #----------------------# # get price and discount price
    our_data = str(t[0])

    our_data = our_data.split('Бренд:')
    description = our_data[0]
    our_data = our_data[1]

    our_data = our_data.split('Цена:')
    our_data = our_data[1]
    our_data = our_data.split('Цена')
    price = our_data[0]
    our_data = our_data[1]

    our_data = our_data.split('по акции:')
    price_discount = our_data[1]

    new_price = ''
    new_discount_price = ''

    for i in price:
        if i.isdigit():
            new_price += i

    for i in price_discount:
        if i.isdigit():
            new_discount_price += i

    price = int(new_price)
    price_discount = int(new_discount_price)
    #----------------------#

    #----------------------#   # get all except price, image, size, title
    k1 = soup.find_all("tr", {"class":"border"})
    new_list =[]
    e1=[]
    e2=[]
    for i in k1:
        new_list.append(i.get_text())

    for i in new_list:
        rrr=i.split(':')
        e1.append(rrr[0])
        e2.append(rrr[1])
    new_dict = dict(zip(e1,e2))
    print(new_dict)

    #----------------------#

    #----------------------# # get image link
    try:
        image = soup.find("div", {"data-id":"img0"})
        yy = str(image)
        yy = yy.split('url(')
        yy = yy[1]
        yy = yy.split(')"')
        yy = yy[0]
        yy = yy.replace('200/','')
        image = 'https://trial-sport.ru' + yy

        f = open(r'C:\python_projects\BikeShop\bike_app\static\bike_app\bike_models\Kidsbikes'
                 + r'\\' + title + ' ' +  new_dict['Год'] + '.' + 'jpg', 'wb')
        f.write(requests.get(image).content)
        f.close()
    except Exception:
        try:
            image = soup.find("div", {"data-id": "color0"})
            yy = str(image)
            yy = yy.split('url(')
            yy = yy[1]
            yy = yy.split(')"')
            yy = yy[0]
            yy = yy.replace('200/', '')
            image = 'https://trial-sport.ru' + yy

            f = open(r'C:\python_projects\BikeShop\bike_app\static\bike_app\bike_models\Kidsbikes'
                     + r'\\' + title + ' ' + new_dict['Год'] + '.' + 'jpg', 'wb')
            f.write(requests.get(image).content)
            f.close()
        except Exception:
            image = 2
            print("IMAGE----ERROR")
    #----------------------# get size
    available_no_size = random.randint(1, 10)
    #----------------------# # Mountbike data
    name = title + ' ' +  new_dict['Год']
    brand = new_dict['Бренд']
    year = int(new_dict['Год'])
    fake_price = price
    price = price_discount
    img_link = name + '.jpg'
    bike_type = 'child_bike'
    #----------------------# # MountbikeDescription data
    description = description
    frame = new_dict['Рама']
    fork = new_dict['Вилка']

    try:
        ammort = new_dict['Задний амортизатор']
    except Exception:
        ammort = 'отсутствует'

    try:
        crank = new_dict['Система']
    except Exception:
        try:
            crank = new_dict['Шатуны']
        except Exception:
            crank = 'отсутствует'

    try:
        pedal = new_dict['Педали']
    except Exception:
        pedal = 'отсутствуют'
    try:
        front_shifter = new_dict['Передний переключатель']
    except Exception:
        front_shifter = 'отсутствует'
    try:
        rear_shifter = new_dict['Задний переключатель']
    except Exception:
        rear_shifter = 'отсутствует'
    try:
        lever = new_dict['Манетки']
    except Exception:
        lever = 'отсутствуют'
    try:
        cassete = new_dict['Кассета']
    except Exception:
        cassete = 'отсутствует'
    try:
        chain = new_dict['Цепь']
    except Exception:
        chain = 'нет'
    try:
        rims = new_dict['Обода']
    except Exception:
        rims = 'нет'
    try:
        tyres = new_dict['Покрышки']
    except Exception:
        tyres = 'нет'
    try:
        front_hub = new_dict['Передняя втулка']
    except Exception:
        front_hub = 'нет'
    try:
        rear_hub = new_dict['Задняя втулка']
    except Exception:
        rear_hub = 'нет'
    try:
        front_brake = new_dict['Передний тормоз']
    except Exception:
        front_brake = 'отсутствует'
    try:
        rear_brake = new_dict['Задний тормоз']
    except Exception:
        rear_brake = 'отсутствует'
    try:
        handlebar = new_dict['Руль']
    except Exception:
        handlebar = 'нет'
    try:
        stem = new_dict['Вынос руля']
    except Exception:
        stem = 'нет'
    try:
        grips = new_dict['Грипсы']
    except Exception:
        grips = 'нет'
    try:
        headset = new_dict['Рулевая колонка']
    except Exception:
        headset = 'нет'
    try:
        saddle = new_dict['Седло']
    except Exception:
        saddle = 'отсутствует'
    try:
        seatpost = new_dict['Подседельный штырь']
    except Exception:
        seatpost = 'отсутствует'

    try:
        print(price, price_discount)
        try:
            MountBikes.objects.get(name=name)
            print('Name Repeat! -- ', name)
            os.remove(r'C:\python_projects\BikeShop\bike_app\static\bike_app\bike_models\Kidsbikes'
                      + r'\\' + title + ' ' + new_dict['Год'] + '.' + 'jpg')
        except:

            if image == 2:
                print('NO IMAGE -- ', image)

            else:
                bike = MountBikes(name=name, brand=brand, year=year, fake_price=fake_price, price=price,
                                  img_link=img_link, bike_type=bike_type, available_no_size=available_no_size,
                                  )

                bikedescription = MountBikesDescription(mountbikes=bike, description=description, frame=frame, ammort=ammort,
                                                        fork=fork, crank=crank, pedal=pedal, front_shifter=front_shifter,
                                                        rear_shifter=rear_shifter, lever=lever, cassete=cassete, chain=chain,
                                                        rims=rims, tyres=tyres, front_hub=front_hub, rear_hub=rear_hub,
                                                        front_brake=front_brake, rear_brake=rear_brake, handlebar=handlebar,
                                                        stem=stem, grips=grips, headset=headset, saddle=saddle,
                                                        seatpost=seatpost, warranty=3,
                                                        )

                bike.save()
                bikedescription.save()
    except Exception as e:
        print('BIKE----SAVE EXCEPTION -- ', e)
        os.remove(r'C:\python_projects\BikeShop\bike_app\static\bike_app\bike_models\Kidsbikes'
                 + r'\\' + title + ' ' + new_dict['Год'] + '.' + 'jpg')




#for mountbikes
# url = 'https://trial-sport.ru/gds.php?s=51516&c1=1070639&c2[]=1070640&age[]=1070483&gender[]' \
#           '=1070509&discount=1&nal[]=str&sizes[]=XL&sizes[]=L&sizes[]=M&sizes[]=S&sizes[]=XS&gpp=100'


#for roadbikes
#url = 'https://trial-sport.ru/gds.php?s=51516&c1=1070639&c2[]=1070790&discount=1&nal[]' \
 #         '=str&sizes[]=S&sizes[]=M&sizes[]=L&sizes[]=XL&gpp=-1'


#for bmx
#url = 'https://trial-sport.ru/gds.php?s=51516&c1=1070639&c2[]=1073338&age[]=1070483&discount=1&nal[]=str&gpp=-1'

#for citybikes
#    url = 'https://trial-sport.ru/gds.php?s=51516&c1=1070639&discount=1&c2%5B%5D=' \
 #         '1078033&price_from=&price_to=&nal%5B%5D=str&sizes%5B%5D=1SZ&sort=0'

###### for migrations #######

from django.db import migrations
from bike_app.parsing import *


def combine_names(apps, schema_editor):
    MountBikes = apps.get_model("bike_app", "MountBikes")
    MountBikesDescription = apps.get_model("bike_app", "MountBikesDescription")

    url = 'https://trial-sport.ru/gds.php?s=51516&c1=1070639&age[]=1070538&discount=1&nal[]=str&sizes[]=1SZ&gpp=-1'

    r = requests.get(url)
    soup = BeautifulSoup(r.content)
    soup.prettify()

    k = soup.find_all("a", {"class": "title"})
    mount_bikes_href = []

    for i in k:
        mount_bikes_href.append(i.get('href'))

    print(mount_bikes_href)

    for i in mount_bikes_href:
        try:
           get_data_kids(i)
        except Exception as e:
            pass
            print('EXCEPTION --- ',e )



class Migration(migrations.Migration):

    dependencies = [
        ('bike_app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(combine_names),
    ]


