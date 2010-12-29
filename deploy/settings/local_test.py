# -*- coding: utf-8 -*-

DEBUG = TEMPLATE_DEBUG = True

ADMINS = (
    ('tech', 'tech@web-mark.ru'),
    ('dgk', 'dgk@web-mark.ru'),
    ('elias', 'elias@web-mark.ru'),
    ('eugene', 'eugene@web-mark.ru'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:', #rel('local.db'),
    },

    'billing': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'billing_test',
        'USER': 'billing_test',
        'PASSWORD': 'akonEsdfsdfd2',
        'HOST': '10.10.10.7',
    },
}

