import os

from kombu import Queue
from django.contrib.messages import constants as messages


PACKAGE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
PROJECT_ROOT = os.path.abspath(os.path.join(PACKAGE_ROOT, os.pardir))
SITE_ROOT = os.path.join(PACKAGE_ROOT, 'site')


# General configuration

DEBUG = True

ADMINS = (('eillarra', 'e@illarra.com'),)
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'DJANGO_SECRET_KEY')
SITE_ID = int(os.environ.get('SITE_ID', 1))

GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY', 'GOOGLE_API_KEY')
OGONE_PSPID = os.environ.get('OGONE_PSPID', 'OGONE_PSPID')
OGONE_SALT = os.environ.get('OGONE_SALT', 'OGONE_SALT')
OGONE_URL = os.environ.get('OGONE_URL', 'OGONE_URL')
PUBLICITY_BOT_PASSWORD = os.environ.get('PUBLICITY_BOT_PASSWORD', 'PUBLICITY_BOT_PASSWORD')
SYMPA_USER = os.environ.get('SYMPA_USER', 'SYMPA_USER')
SYMPA_PASSWORD = os.environ.get('SYMPA_PASSWORD', 'SYMPA_PASSWORD')

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.flatpages',
    'django.contrib.messages',
    'django.contrib.redirects',
    'django.contrib.sessions',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'raven.contrib.django.raven_compat',
    'whitenoise.runserver_nostatic',

    # theme
    'captcha',
    'compressor',
    'crispy_forms',

    # auth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.linkedin_oauth2',

    # api
    'corsheaders',
    'rest_framework',

    # app
    'hipeac',
    'hipeac.api',
    'hipeac.site',

    # admin
    'anymail',
    'django.contrib.admin',
]

MIDDLEWARE = [
    'raven.contrib.django.raven_compat.middleware.SentryResponseErrorIdMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'dnt.middleware.DoNotTrackMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

ROOT_URLCONF = 'hipeac.urls'
WSGI_APPLICATION = 'hipeac.wsgi.app'

FIXTURE_DIRS = [
    os.path.join(PROJECT_ROOT, 'fixtures'),
]


# Time zones
# https://docs.djangoproject.com/en/2.0/topics/i18n/timezones/

USE_TZ = True
TIME_ZONE = 'Europe/Brussels'


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en'
USE_I18N = False
USE_L10N = False

FIRST_DAY_OF_WEEK = 1
DATE_FORMAT = 'N j, Y'
TIME_FORMAT = 'H:i'
DATETIME_FORMAT = DATE_FORMAT + ', ' + TIME_FORMAT


# Security / Accounts
# https://django-allauth.readthedocs.io/en/latest/

CORS_ORIGIN_ALLOW_ALL = True

LOGOUT_REDIRECT_URL = '/'

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'

SOCIALACCOUNT_PROVIDERS = {
    'linkedin': {
        'SCOPE': [
            'r_emailaddress',
        ],
        'PROFILE_FIELDS': [
            'id',
            'first-name',
            'last-name',
            'email-address',
            'picture-url',
            'public-profile-url',
        ]
    }
}


# CSRF / Cookie

SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG
CSRF_USE_SESSIONS = not DEBUG

# XFRAME

X_FRAME_OPTIONS = 'DENY'


# http://www.django-rest-framework.org/api-guide/settings/

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',
    'DEFAULT_VERSION': 'v1',
    'PAGE_SIZE': 50,
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
}


# https://docs.djangoproject.com/en/2.1/topics/templates/

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(SITE_ROOT, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
                'hipeac.context_processors.git_rev',
            ],
        },
    },
]

MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
# https://docs.djangoproject.com/en/2.0/howto/static-files/deployment/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(SITE_ROOT, 'www', 'static')
STATICFILES_DIRS = (
    os.path.join(SITE_ROOT, 'static'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'compressor.finders.CompressorFinder',
)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

COMPRESS_OFFLINE = True
COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)


# File uploads
# https://docs.djangoproject.com/en/1.11/topics/http/file-uploads/

FILE_UPLOAD_PERMISSIONS = 0o644


# wkhtmltopdf requires MEDIA configuration to be set
# http://stackoverflow.com/questions/24071290/
# https://docs.djangoproject.com/en/2.0/ref/settings/#media-root

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(SITE_ROOT, 'www', 'media')


# http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html#celerytut-configuration

task_default_queue = 'hipeac'
CELERY_TASK_QUEUES = [Queue(name=task_default_queue)]
CELERY_TASK_DEFAULT_QUEUE = task_default_queue

CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CELERY_TIMEZONE = TIME_ZONE
CELERY_ENABLE_UTC = False


# reCAPTCHA
# https://github.com/praekelt/django-recaptcha#installation

RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY', 'RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_PRIVATE_KEY', 'RECAPTCHA_PRIVATE_KEY')
RECAPTCHA_USE_SSL = True
NOCAPTCHA = True  # For using reCAPTCHA v2


# https://django-crispy-forms.readthedocs.io/en/latest/index.html

CRISPY_TEMPLATE_PACK = 'bootstrap4'
CRISPY_FAIL_SILENTLY = False


COUNTRIES_OVERRIDE = {
    'US': 'United States',
}
