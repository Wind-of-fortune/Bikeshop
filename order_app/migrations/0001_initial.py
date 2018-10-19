# Generated by Django 2.1.1 on 2018-10-18 19:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('item_name', models.CharField(max_length=100)),
                ('item_code', models.PositiveIntegerField(null=True)),
                ('item_size', models.CharField(max_length=2)),
                ('item_price', models.PositiveIntegerField()),
                ('mark', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('order_item_name', models.CharField(max_length=1000)),
                ('order_item_size', models.CharField(max_length=200)),
                ('items_price', models.CharField(max_length=1000)),
                ('sum_price', models.BigIntegerField()),
                ('ship_country', models.CharField(default='Russia', max_length=100)),
                ('ship_city', models.CharField(default='Irkutsk', max_length=100)),
                ('ship_street', models.CharField(max_length=100)),
                ('ship_house', models.CharField(max_length=100)),
                ('ship_postalcode', models.CharField(max_length=20)),
                ('contact_phone', models.CharField(max_length=30)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_delivered', models.DateTimeField(null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_paid', models.BooleanField(default=False)),
                ('is_accept', models.BooleanField(default=False)),
                ('add_information', models.CharField(blank=True, max_length=1000)),
            ],
        ),
    ]
