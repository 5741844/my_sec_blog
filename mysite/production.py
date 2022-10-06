from .base import *

ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com', '130.193.36.152'] # customize with your domain name

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'djangogirls',
        'USER': 'ad2',
        'PASSWORD': '7fekzhbjy',
        'HOST': 'localhost',
        'PORT': '',
    }
}

STATIC_ROOT = '/home/ad2/static'
MEDIA_ROOT = '/home/ad2/media'
