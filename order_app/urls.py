from django.urls import path
from bike_app.views import *

app_name = 'bike_app'

urlpatterns = [
    path('', main_page, name='main_page'),

]
