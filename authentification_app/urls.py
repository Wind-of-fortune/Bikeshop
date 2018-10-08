from django.urls import path
from django.views.generic import CreateView
from authentification_app.forms import UserRegistartionForm

from authentification_app.views import *

app_name = 'authentification_app'

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', user_register, name='register'),

    # path('login/register/', CreateView.as_view(
    #     template_name='authentification_app/register.html',
    #     form_class=UserRegistartionForm,
    #     success_url='/success' ), name='register'),
    #
    # path('success/', register, name = 'register_success'),

]
