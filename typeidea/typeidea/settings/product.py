# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: product
@time:2023/6/21
@Author:majiaqin 170479
@Desc:生产环境配置
'''
from .base import *

DEBUG = False

ALLOWED_HOSTS = ['the5fire.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'typeidea_db',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'CONN_MAX_AGE': 60,
        'OPTIONS': {'charset': 'utf8mb4'}
        },
}

ADMINS = MANAGERS = (
    ('姓名', '<邮件地址>'),
)

EMAIL_HOST = '<邮件SMTP服务地址>'
EMAIL_HOST_USER = '<邮箱登录名>'
EMAIL_HOST_PASSWORD = '<邮箱登录密码>'
EMAIL_SUBJECT_PREFIX = '<邮件标题前缀>'
DEFAULT_FROM_EMAIL = '<邮件展示发件人地址>'
SERVER_EMAIL = '<邮件服务器>'

STATIC_ROOT = '/home/the5fire/venvs/typeidea-env/static_files/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(levelname)s %(asctime)s %(module)s:'
                      '%(funcName)s %(lineno)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/tmp/logs/typeidea.log',
            'formatter': 'default',
            'maxBytes': 1024*1024,
            'backupCount': 5,
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}

REDIS_URL = '127.0.0.1:6379:1'

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': REDIS_URL,
        'TIMEOUT': 300,
        'OPTIONS': {
            'PASSWORD': 'password',
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'PARSER_CLASS': 'redis.connection.HiredisParser',
        },
        'CONNECTION_POOL_CLASS': 'redis.connection.BlockingConnectionPool',
    }
}