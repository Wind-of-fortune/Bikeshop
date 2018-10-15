from django.urls import path
from order_app.views import *

app_name = 'order_app'

urlpatterns = [
    path('basket/', basket, name='basket'),
    path('makeorder/', make_order, name='make_order'),
    path('makeorderall/', make_order_all, name='make_order_all'),
    path('deleteorder/', delete_order, name='delete_order'),
    path('submitorder/', submit_order, name='submit_order'),
]
