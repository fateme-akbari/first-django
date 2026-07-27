from firstdjango.settings import *

# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

#SECRET_KEY 
DEBUG = False

ALLOWED_HOSTS = []

SITE_ID = 2

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

MEDIA_ROOT = BASE_DIR / "media"
STATC_ROOT = BASE_DIR / "static"
STATICFILES_DIRS = [
    BASE_DIR / "statics",
]

CSRF_COOKIE_SECURE = True