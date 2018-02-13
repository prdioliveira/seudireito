from .base import *
import sys

ENV = 'TEST'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
SERVER_PORT = 8000

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Parse database configuration from $DATABASE_URL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'seuDireitoTest'
    }
}