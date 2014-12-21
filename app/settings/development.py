from .base import *


MIDDLEWARE_CLASSES += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INSTALLED_APPS += [
    "debug_toolbar",
]


DATABASES['default']['OPTIONS'] = {}