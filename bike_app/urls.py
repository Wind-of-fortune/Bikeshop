
from django.urls import path
from bike_app.views import *

app_name = 'bike_app'

urlpatterns = [
    path('', main_page, name='main_page'),
    path('mountbike/', mountbike, name='mountbike'),
    path('mountbike/name/', mountbike_model, name='mountbike_model'),
    path('roadbike/', mountbike, name='roadbike'),
    path('roadbike/name/', mountbike_model, name='roadbike_model'),
    path('bmxbike/', mountbike, name='bmxbike'),
    path('bmxbike/name/', mountbike_model, name='bmxbike_model'),
    path('bmxbike/name2/', bmxbike_model, name='bmxbike_model2'),
    path('citybike/', mountbike, name='citybike'),
    path('citybike/name/', mountbike_model, name='citybike_model'),
    path('citybike/name2/', bmxbike_model, name='citybike_model2'),
    path('kidsbike/', mountbike, name='kidsbike'),
    path('kidsbike/name/', mountbike_model, name='kidsbike_model'),
    path('kidsbike/name2/', bmxbike_model, name='kidsbike_model2'),
]
