import dj_database_url

from .base import *


ALLOWED_HOSTS = ['*']

# configuración según documentación de heroku
# para usar postgres: 
# https://devcenter.heroku.com/articles/connecting-heroku-postgres#connecting-with-django
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)
