import os
import logging

DOMAIN = 'http://ci-project.appspot.com'

DATABASE_ENGINE = '' 
DATABASE_NAME = ''
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = ''

TIME_ZONE = 'UTC'

LANGUAGE_CODE = 'en-us'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

ROOT_URLCONF = 'urls'
ROOT_PATH = os.path.dirname(__file__)
TEMPLATE_DIRS = (
    os.path.join(ROOT_PATH, 'templates')
)

TEMPLATE_CONTEXT_PROCESSORS = (
                               "django.core.context_processors.i18n",
                               )

MIDDLEWARE_CLASSES = (
                      'google.appengine.ext.ndb.django_middleware.NdbDjangoMiddleware',
                      'django.contrib.sessions.middleware.SessionMiddleware',
                      )

logging.getLogger().setLevel(logging.DEBUG)