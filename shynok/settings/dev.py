from .base import *


SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "django-insecure-%7mmqzyin+4o6=djc+blg4h!3sp)hbs$po_2x6-3n@3c&3h_f9")


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
