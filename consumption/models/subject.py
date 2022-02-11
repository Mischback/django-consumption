# SPDX-License-Identifier: MIT

"""Provide the app's main class that actually represent a consumer."""

# Django imports
from django import forms
from django.db import models
from django.utils.translation import gettext_lazy as _


class Subject(models.Model):
    """Represent a consumer."""

    name = models.CharField(
        max_length=100,
        help_text=_("The human-readable identifier for instances of Subject"),
        verbose_name=_("Subject Name"),
    )
    """The human-readable identifier for instances of this class."""

    class Meta:  # noqa: D106
        app_label = "consumption"
        verbose_name = _("Subject")
        verbose_name_plural = _("Subjects")

    def __str__(self):  # noqa: D105
        return "{} ({})".format(self.name, self.id)  # pragma: nocover


class SubjectForm(forms.ModelForm):
    """Get and validate input for creating and updating ``Subject`` instances."""

    template_name = "consumption/forms/generic.html"
    """This template will be used to render the form.

    This uses Django's form rendering, as introduced in v4.0, see
    :djangoapi:`Outputting forms as HTML <forms/api/#ref-forms-api-outputting-html>`.
    """

    class Meta:  # noqa: D106
        model = Subject
        fields = "__all__"
