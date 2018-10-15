from django.urls import path

from authentification_app.views import *

app_name = 'authentification_app'

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', user_register, name='register'),
    path('register2/', user_register_part2, name='register2'),
    path('passwordchange/', password_change, name='password_change'),
    path('delete/', delete_account, name='delete_account'),
    path ('ls/', ls, name = 'ls'),
    path('useractiveorders/', user_active_orders, name='user_active_orders'),
    path('userfinishedorders/', user_finished_orders, name='user_finished_orders'),
    # path('login/register/', CreateView.as_view(
    #     template_name='authentification_app/register.html',
    #     form_class=UserRegistartionForm,
    #     success_url='/success' ), name='register'),
    #
    # path('success/', register, name = 'register_success'),

]
