# Generated by Django 2.1.1 on 2018-09-28 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mountbikesdescription',
            name='warranty',
            field=models.PositiveSmallIntegerField(default=5),
        ),
    ]