from django.urls import path
from order_app.views import *

app_name = 'order_app'

urlpatterns = [
    path('basket/', basket, name='basket'),
    path('makeorder/', make_order, name='make_order'),

]
