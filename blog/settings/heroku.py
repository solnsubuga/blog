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


DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_S3_ENDPOINT_URL = config('AWS_S3_ENDPOINT_URL')

AWS_S3_REGION_NAME = config('AWS_S3_REGION_NAME')

AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')

AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')

AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')

AWS_DEFAULT_ACL = None

AWS_QUERYSTRING_AUTH = False

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
