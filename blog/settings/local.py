from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME_L'),
        'USER': os.environ.get('DB_USER_L'),
        'PASSWORD': os.environ.get('DB_PWD_L'),
        'HOST': os.environ.get('DB_HOST_L'),
        'PORT': os.environ.get('DB_PORT_L'),
    }
}
