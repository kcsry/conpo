import os

from environ import Env

env = Env()
DEBUG = env.bool('DEBUG', default=False)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
assert os.path.exists(os.path.join(BASE_DIR, 'manage.py'))
VAR_DIR = os.path.join(BASE_DIR, 'var')
os.makedirs(VAR_DIR, exist_ok=True)
SECRET_KEY = env.str('SECRET_KEY', ('x' if DEBUG else Env.NOTSET))
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['*'])
ROOT_URLCONF = 'conpo_project.urls'
WSGI_APPLICATION = 'conpo_project.wsgi.application'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(VAR_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(VAR_DIR, 'media')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'conpo.core',
    'conpo.api',
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
DATABASES = {
    'default': env.db_url('DATABASE_URL', default='sqlite:///%s' % os.path.join(VAR_DIR, 'db.sqlite3')),
}
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
