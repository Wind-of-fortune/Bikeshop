# BikeShop URL Configuration

from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.urls import include

from bike_app import urls as bike_urls
from authentification_app import urls as authentification_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bike/', include((bike_urls, 'bike_app'), namespace='bike')),
    path('auth/', include((authentification_urls, 'authentification_app'), namespace='authentification_app')),
]

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += [
#         path('__debug__/', include(debug_toolbar.urls)),
#     ]
#
