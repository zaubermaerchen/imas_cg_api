from api.settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'imas_cg',  # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'imas_cg',
        'PASSWORD': 'imas_cg',
        'HOST': 'localhost',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '3306',  # Set to empty string for default.
    }
}

#CACHES = {
#    'default': {
#        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
#        'LOCATION': 'localhost:11211',
#    }
#}