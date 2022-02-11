# SPDX-License-Identifier: MIT

"""Django settings for the development setup.

This module extends the settings of the test suite (tests.util.settings) with
development-specific values.
"""

# app imports
from tests.util.settings_test import *  # noqa: F403

# Enable Django's DEBUG mode
DEBUG = True
ALLOWED_HOSTS = ["*"]


INSTALLED_APPS += [  # noqa: F405
    # activate django-debug_toolbar
    "debug_toolbar",
]

MIDDLEWARE += [  # noqa: F405
    # add DebugToolbar middleware
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

# development specific extensions for the minimal setup
ROOT_URLCONF = "tests.util.urls_dev"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "dev.sqlite3",  # noqa: F405
    }
}

# specific for debug_toolbar
DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": "dev_env.callback_show_debug_toolbar",
}

# Minimal logging configuration for the app
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "dev_f": {
            "format": "[%(levelname)s] %(name)s:%(lineno)d:%(funcName)s \n\t %(message)s",
        },
    },
    "handlers": {
        "def_h": {
            "class": "logging.StreamHandler",
            "formatter": "dev_f",
        },
    },
    "loggers": {
        "consumption": {
            "handlers": ["def_h"],
            "level": "DEBUG",
            "propagate": False,
        }
    },
}
