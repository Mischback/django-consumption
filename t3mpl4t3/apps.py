# SPDX-License-Identifier: MIT

"""Application configuration as required by Django."""

# Python imports
import logging

# Django imports
from django.apps import AppConfig

# get a module-level logger
logger = logging.getLogger(__name__)


class t3mpl4t3Config(AppConfig):
    """Application-specific configuration class, as required by Django.

    This sub-class of Django's ``AppConfig`` provides application-specific
    information to be used in Django's application registry (see
    :djangoapi:`Configuring Applications <applications/#configuring-applications>`).
    """

    name = "t3mpl4t3"
    verbose_name = "t3mpl4t3"
