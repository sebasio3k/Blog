from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'django-blog-hodev.herokuapp.com',
]

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dc0ckpt5hr14p3',
        'USER': 'wjoqvvvmpsmhln',
        'PASSWORD': '    9eb0d95099e0981f514a9fa8b8f26a4f384778397f3ffbdee50b1592c813a6c1',
        'HOST': 'ec2-54-86-224-85.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}
