"""Django settings for trocgraines project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path
from django.contrib.messages import constants as messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'trocgraines',
    'authentication',
    'seeds',
    'crispy_forms',
    'cloudinary_storage',
    'cloudinary',
    'imagekit',
    'exchange_messages',
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

ROOT_URLCONF = 'trocgraines_config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'trocgraines_config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
	'ENGINE': 'django.db.backends.postgresql',
	'NAME': os.environ['DATABASES_NAME'],
	'USER': os.environ['DATABASES_USER'],
	'PASSWORD': os.environ['DATABASES_PASSWORD'],
	'HOST': 'localhost',
	'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
            'django.contrib.auth.password_validation.'
            'UserAttributeSimilarityValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.'
            'MinimumLengthValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.'
            'CommonPasswordValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.'
            'NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'fr'
TIME_ZONE = 'Europe/Paris'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# Media files

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# authentication

AUTH_USER_MODEL = 'authentication.User'
LOGIN_URL = 'authentication:login'
LOGIN_REDIRECT_URL = 'trocgraines:homepage'
LOGOUT_REDIRECT_URL = 'trocgraines:homepage'

# crispy_forms

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = os.environ['EMAIL_HOST'] #'smtp.free.fr'
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER'] #'youremail@free.fr'
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD'] #'email_password'
EMAIL_PORT = os.environ['EMAIL_PORT']
DEFAULT_FROM_EMAIL = os.environ['DEFAULT_FROM_EMAIL'] #'youremail@free.fr'

# change django message tags to match bootstrap tags
MESSAGE_TAGS = {
    messages.DEBUG: 'info',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}
