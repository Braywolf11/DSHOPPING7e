from .core import *
DEBUG = True

ALLOWED_HOSTS = []
# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dshopping',
        'USER': 'postgres',
        'PASSWORD': 'unicesmag',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
STATICFILES = (BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
