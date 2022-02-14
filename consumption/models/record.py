# SPDX-License-Identifier: MIT

"""Provide the app's class to represent one type of consumed resource."""

# Django imports
from django import forms
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# app imports
from consumption.models.resource import Resource


class Record(models.Model):
    """Represent one measuring of a :class:`~consumption.models.resource.Resource`."""

    resource = models.ForeignKey(
        to=Resource,
        on_delete=models.CASCADE,
        help_text=_("The resource to provide this record for"),
        verbose_name=_("Resource Instance"),
    )
    """The resource to provide this record for."""

    reading = models.FloatField(
        help_text=_("The actual numerical value, without its unit"),
        verbose_name=_("Reading"),
    )
    """The actual numerical value, without its unit."""

    timestamp = models.DateTimeField(
        help_text=_("Date and Time of the record"),
        verbose_name=_("Date/Time of the record"),
    )
    """Date and Time of the record."""

    class Meta:  # noqa: D106
        app_label = "consumption"
        verbose_name = _("Record")
        verbose_name_plural = _("Records")

    def __str__(self):  # noqa: D105
        return "{}: {} ({}, {})".format(
            self.timestamp, self.reading, self.resource.unit, self.resource.name
        )

    def get_absolute_url(self):
        """Return the absolute URL for instances of this model.

        This may be considered the *default* URL for this model.
        """
        return reverse("consumption:record-detail", args=[self.id])  # pragma: nocover


class RecordForm(forms.ModelForm):
    """Get and validate input for creating and updating ``Record`` instances."""

    template_name = "consumption/forms/generic.html"
    """This template will be used to render the form.

    This uses Django's form rendering, as introduced in v4.0, see
    :djangoapi:`Outputting forms as HTML <forms/api/#ref-forms-api-outputting-html>`.
    """

    class Meta:  # noqa: D106
        model = Record
        fields = "__all__"
