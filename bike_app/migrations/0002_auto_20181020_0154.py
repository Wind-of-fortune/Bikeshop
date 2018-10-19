
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


