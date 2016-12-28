from channel2600.settings import *
import dj_database_url

DEBUG=False
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFileStorage'
