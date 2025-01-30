import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'crud',
        'USER': 'openpg',
        'PASSWORD': 'openpgpwd',
        'HOST': 'localhost',
        'PORT': '5432',
        'OPTIONS': {'sslmode':'disable'},
    }
}
