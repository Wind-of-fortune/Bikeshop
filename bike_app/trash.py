import uuid

from django.core.mail import send_mail

def email_for_registration():
    code_for_registration = str(uuid.uuid4())
    send_mail(
        'Здравствуйте!!!',

        'Вас приветствует магазин BikeShop, код для продолжения регистрации {}, '
        'если вы у нас не регистрировались, '
        'то просто игнорируйте это сообщение'.format(code_for_registration),

        'Wind-of-fortune2@yandex.ru',
        ['Wind-of-fortune2@yandex.ru'],
        fail_silently=False,
    )