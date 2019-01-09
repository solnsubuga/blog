"""Configuration settings for heroku deployment
"""

from .base import *

import dj_database_url
from decouple import config

DEBUG = False

ALLOWED_HOSTS = ['authors-app.herokuapp.com']

DATABASES = {
    'default': dj_database_url.config(default=config('DATABASE_URL'))
}
