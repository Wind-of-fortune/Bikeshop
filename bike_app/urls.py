
from django.urls import path
from bike_app.views import *

urlpatterns = [
    path('', main_page, name='main_page'),
    path('mountbike/', mountbike, name='mountbike'),
    # path('mountbike/sorted/available', mountbike_sort_by_available, name='mountbike_sort_by_available'),
    # path('mountbike/sorted/pricelow', mountbike_sort_by_price_low_to_high, name='mountbike_sort_by_price_low_to_high'),
    # path('mountbike/sorted/pricehigh', mountbike_sort_by_price_high_to_low, name='mountbike_sort_by_price_high_to_low'),
    # path('mountbike/sorted/brand', mountbike_sort_by_brand, name='mountbike_sort_by_brand'),
]
