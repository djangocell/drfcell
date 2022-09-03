import dj_database_url
import os
import platform
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = "django-insecure-rbju9+0)tn6f8jiv35oomj#z%*7#(zsl)4foe6qhevmejjzkzf"
DEBUG = False
ALLOWED_HOSTS = ["*"]


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
ROOT_URLCONF = "settings.urls"

TEMPLATES = [{"BACKEND": "django.template.backends.django.DjangoTemplates",
              "DIRS": [],
              "APP_DIRS": True,
              "OPTIONS": {"context_processors": ["django.template.context_processors.debug",
                                                 "django.template.context_processors.request",
                                                 "django.contrib.auth.context_processors.auth",
                                                 "django.contrib.messages.context_processors.messages"]
                          }
              }]

WSGI_APPLICATION = "settings.wsgi.application"

DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3',
                         'NAME': BASE_DIR / 'db.sqlite3'}}


AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"}
]

LANGUAGE_CODE = "ko-kr"
TIME_ZONE = "Asia/Seoul"
USE_I18N = True
USE_L10N = True
USE_TZ = False

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

if platform.system() != "Windows":
    MIDDLEWARE.append("whitenoise.middleware.WhiteNoiseMiddleware")
    STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"
    DATABASES = {'default': {'ENGINE': 'django.db.backends.postgresql_psycopg2',
                             'NAME': 'cell',
                             'USER': 'admin',
                             'PASSWORD': '1234',
                             'HOST': 'localhost',
                             'PORT': '5432'}}
    db_from_env = dj_database_url.config(conn_max_age=500)
    DATABASES['default'].update(db_from_env)
