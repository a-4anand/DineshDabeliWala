from pathlib import Path
import os
from django.contrib.messages import constants as messages

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure--&()dt)+zdqa$sc+un^admluii%2_2bsynrz1382wjq1wh5b=d"

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    "dabeli.apps.DabeliConfig",
    "custom_admin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'django.middleware.csrf.CsrfViewMiddleware',
]

ROOT_URLCONF = "dukan.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "dukan.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


CSRF_TRUSTED_ORIGINS = [
    "https://dineshdabeli.up.railway.app/",
    "https://dineshdabeli.great-site.net",
    'https://dineshdabeliwala.onrender.com',
    'https://dineshdabeli.up.railway.app',
    'https://www.dineshdabeli.up.railway.app',
    
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True
USE_TZ = True

STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "dabeli", "static")]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

