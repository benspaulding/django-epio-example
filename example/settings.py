# Django settings for ep.io example project.
import os

try:
    # ep.io has package that provides a dictionary of information about
    # your deployement, such as database and redis settings.
    # See https://www.ep.io/docs/services/
    from bundle_config import config
except ImportError:
    raise ImportError('bungle_config cannot be imported. Are you on ep.io?')


# Use this to point to media and template resources in our project.
PROJ_ROOT = os.path.dirname(os.path.realpath(__file__))

# A writable storage area is located at ~/data/
# See https://www.ep.io/docs/importexport/#writable-storage
DATA_DIR = config['core']['data_directory']

# Redis settings provided by bundle_config.config.
REDIS_HOST = config['redis']['host']
REDIS_PORT = config['redis']['port']
REDIS_PASSWORD = config['redis']['password']
REDIS_DB = 0

# DEBUG = TEMPLATE_DEBUG = True
ADMINS = MANAGERS = (
    ('Your Awesome Self', 'awesome@example.com'),
)
INTERNAL_IPS = (
    '127.0.0.1',
)

ROOT_URLCONF = 'example.urls'
SECRET_KEY = 'nn1l!&ehsd*upc5)4m8k!^c9j35=20s97kcit7iasz*)&oj5)p'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
ADMIN_FOR = (__name__, )

# DATABASES ?!
# Notice that there are not database settings here. That is because
# ep.io appends the automatically. That can be turned off in the
# epio.ini file.
# NOTE that you will need to turn it off and add database settings on
# your own using bundle_config if you have a non-standard settings
# arrangement.
# See https://www.ep.io/docs/epioini/#epioini-append-settings

# Point media root to the writable storage.
MEDIA_ROOT = '%s/media/' % DATA_DIR
MEDIA_URL = '/media/'

# Point static root, where static media is collected to, at the
# writable storage.
STATIC_ROOT = '%s/static/' % DATA_DIR
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    '%s/static/' % PROJ_ROOT,
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder', # Default
    'django.contrib.staticfiles.finders.AppDirectoriesFinder', # Default
    'compressor.finders.CompressorFinder', # Need this for compressor.
)

CACHES = {
    'default': {
        # File caching could be used by pointing it at the writatble storage.
        # 'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        # 'LOCATION': '%s/cache/' % DATA_DIR,

        # But using Redis is more awesome.
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': '%s:%s' % (REDIS_HOST, REDIS_PORT),
        'OPTIONS': {
            'DB': REDIS_DB,
            'PASSWORD': REDIS_PASSWORD,
        },
        'KEY_PREFIX': 'example',
        'TIMEOUT': 600,
    },
}
CACHE_MIDDLEWARE_KEY_PREFIX = 'example_m'
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True

# Sessions could also be file-based.
# SESSION_ENGINE = 'django.contrib.sessions.backends.file'
# SESSION_FILE_PATH = '%s/sessions/' % DATA_DIR

# But, again, Redis has more awesome.
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

# Redis!
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

# You will need to set email on another service. ep.io does not handle it.
# See https://www.ep.io/docs/runtime/#email
DEFAULT_FROM_EMAIL = 'webmaster@localhost'
EMAIL_SUBJECT_PREFIX = '[ep.io Example] '

TEMPLATE_DIRS = (
    '%s/templates/' % PROJ_ROOT,
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',                    # First
    'django.middleware.gzip.GZipMiddleware',                            # First after cache, so gzipping is the last thing that happens to the response.
    'django.middleware.common.CommonMiddleware',                        # 1
    'django.middleware.locale.LocaleMiddleware',                        # ?
    'django.contrib.sessions.middleware.SessionMiddleware',             # 2 Before Messages
    # 'django.middleware.csrf.CsrfViewMiddleware',                      # 3 Don't need to install this unless writing POST views.
    'django.contrib.auth.middleware.AuthenticationMiddleware',          # 4
    'django.contrib.messages.middleware.MessageMiddleware',             # 5 After Session
    'django.middleware.doc.XViewMiddleware',                            # After Common, Session and Auth.
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',   # Last before cache
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',   # Last before cache
    'django.middleware.transaction.TransactionMiddleware',              # Very last before cache
    'django.middleware.cache.FetchFromCacheMiddleware',                 # Last
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.flatpages',
    'django.contrib.humanize',
    'django.contrib.messages',
    'django.contrib.redirects',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'example.apps.things',
    'compressor',
    'haystack',
)

COMPRESS_ENABLED = True
COMPRESS_OUTPUT_DIR = 'c'
COMPRESS_CSS_FILTERS = (
    'compressor.filters.css_default.CssAbsoluteFilter', # Default
    'compressor.filters.cssmin.CSSMinFilter',
    'compressor.filters.datauri.CssDataUriFilter',
)

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': '%s/indexes/' % DATA_DIR,
        'INCLUDE_SPELLING': True,
    },
}
