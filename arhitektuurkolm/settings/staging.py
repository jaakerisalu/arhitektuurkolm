from settings.base import *


DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['TODO.com']

# Static site url, used when we need absolute url but lack request object, e.g. in email sending.
SITE_URL = 'http://TODO.com'

EMAIL_HOST_PASSWORD = 'TODO (api key)'


STATIC_URL = '/assets/'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'KEY_PREFIX': 'arhitektuurkolm',
    }
}

# Production logging - all INFO and higher messages go to info.log file. ERROR and higher messages additionally go to
#  error.log file plus to Sentry.
LOGGING['handlers'] = {
    'info_log': {
        'level': 'INFO',
        'class': 'logging.handlers.WatchedFileHandler',
        'filename': '/var/log/arhitektuurkolm/info.log',
        'formatter': 'default',
    },
    'error_log': {
        'level': 'ERROR',
        'class': 'logging.handlers.WatchedFileHandler',
        'filename': '/var/log/arhitektuurkolm/error.log',
        'formatter': 'default',
    },
    'sentry': {
        'level': 'ERROR',
        'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
    },
}
LOGGING['loggers'][''] = {
    'handlers': ['info_log', 'error_log', 'sentry'],
    'level': 'INFO',
    'filters': ['require_debug_false'],
}

# Sentry error logging
INSTALLED_APPS += (
    'raven.contrib.django.raven_compat',
)
RAVEN_BACKEND_DSN = 'https://TODO:TODO@sentry.thorgate.eu/TODO'
RAVEN_CONFIG['dsn'] = RAVEN_BACKEND_DSN
