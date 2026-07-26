"""
Production settings for Farm project.
"""

from .base import *


# ==========================================================
# SECURITY
# ==========================================================

SECRET_KEY = "CHANGE_THIS_IN_ENV"

DEBUG = False

ALLOWED_HOSTS = [
    "your-domain.com",
    "www.your-domain.com",
]


# ==========================================================
# DATABASE
# ==========================================================

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "farm",
        "USER": "postgres",
        "PASSWORD": "CHANGE_ME",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}


# ==========================================================
# EMAIL
# ==========================================================

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = "smtp.your-provider.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""


# ==========================================================
# SECURITY HEADERS
# ==========================================================

SECURE_BROWSER_XSS_FILTER = True

SECURE_CONTENT_TYPE_NOSNIFF = True

X_FRAME_OPTIONS = "DENY"

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

SECURE_SSL_REDIRECT = True


# ==========================================================
# STATIC FILES
# ==========================================================

STATICFILES_STORAGE = (
    "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"
)


# ==========================================================
# CACHE
# ==========================================================

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    }
}