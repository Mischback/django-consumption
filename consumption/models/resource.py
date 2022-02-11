# SPDX-License-Identifier: MIT

"""Provide the app's class to represent one type of consumed resource."""

# Django imports
from django.db import models
from django.utils.translation import gettext_lazy as _

# app imports
from consumption.models.subject import Subject


class Resource(models.Model):
    """Represent a resource consumed by a :class:`~consumption.models.subject.Subject`."""

    name = models.CharField(
        max_length=50,
        help_text=_("The name of this resource"),
        verbose_name=_("Resource Name"),
    )
    """The name of the resource."""

    subject = models.ForeignKey(
        to=Subject,
        on_delete=models.CASCADE,
        help_text=_("The subject to track this resource for"),
        verbose_name=_("Subject Instance"),
    )
    """The subject to track this resource for."""

    description = models.TextField(
        help_text=_("An optional description for this resource"),
        verbose_name=_("Resource Description"),
        blank=True,
    )
    """An optional description of this resource."""

    unit = models.CharField(
        max_length=25,
        help_text=_("The unit of measurement for this resource"),
        verbose_name=_("Unit of Measurement"),
    )
    """The unit of measurement for this resource."""

    class Meta:  # noqa: D106
        app_label = "consumption"
        verbose_name = _("Resource")
        verbose_name_plural = _("Resources")

    def __str__(self):  # noqa: D105
        return "{} ({}, {}) [{}]".format(
            self.name, self.unit, self.subject.id, self.id
        )  # pragma: nocover
