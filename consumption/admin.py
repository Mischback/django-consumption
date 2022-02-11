# SPDX-License-Identifier: MIT

"""Integrates the app's models into Django's admin interface."""

# Django imports
from django.contrib import admin

# app imports
from consumption.models import Subject


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    """Provide (most-basic) integration into Django's admin interface."""
