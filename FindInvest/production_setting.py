from .settings import *
import dj_database_url 

DATABASES['default'] = dj_database_url.config()

DEBUG = False
TEMPLATE_DEBUG = False

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware',]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


SECRET_KEY = 'uyp1wld474qu#gnfvtvl%yo93cvg_ko1*j-)py5*u(i5lmi3v%'

ALLOWED_HOSTS = ['findinvests.herokuapp.com']