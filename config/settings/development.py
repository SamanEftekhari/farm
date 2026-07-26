"""
Development settings for Farm project.
"""

from .base import *


# ==========================================================
# SECURITY
# ==========================================================

SECRET_KEY = "django-insecure-change-this-key"

DEBUG = True

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]


# ==========================================================
# DATABASE
# ==========================================================

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# ==========================================================
# EMAIL
# ==========================================================

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


# ==========================================================
# CACHE
# ==========================================================

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    }
}