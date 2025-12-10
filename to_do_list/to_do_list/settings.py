"""
Django settings for to_do_list project.
"""

from pathlib import Path
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-g1cd9m(y96542jwnt^1#6+6&@%hk0f+(dd-v#d&4^mgn3uw-qz'
DEBUG = True
ALLOWED_HOSTS = []


# -------------------- INSTALLED APPS --------------------

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',

    # Your app
    'apibackendapp',
]


# -------------------- MIDDLEWARE --------------------

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # CORS middleware MUST be above CommonMiddleware
    'corsheaders.middleware.CorsMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',

    # CSRF stays enabled — but we will disable it PER VIEW using csrf_exempt
    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'to_do_list.urls'


# -------------------- TEMPLATES --------------------

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'to_do_list.wsgi.application'


# -------------------- DATABASE --------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'to_do_list_2025',
        'USER': 'root',
        'PASSWORD': 'Ashna@23',
        'HOST': 'localhost',
        'PORT': 3306,
    }
}


# -------------------- PASSWORD VALIDATION --------------------

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# -------------------- INTERNATIONALIZATION --------------------

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True



# -------------------- STATIC FILES --------------------

STATIC_URL = 'static/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# -------------------- REST FRAMEWORK CONFIG --------------------

REST_FRAMEWORK = {
    # This allows frontend POSTs without CSRF issues
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),

    # Default: Allow all unless overridden in views
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.AllowAny",
    ),
}



# -------------------- JWT SETTINGS --------------------

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}



# -------------------- CORS SETTINGS --------------------

CORS_ALLOW_ALL_ORIGINS = True
