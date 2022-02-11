# SPDX-License-Identifier: MIT

"""Provide the app's main class that actually represent a consumer."""

# Django imports
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
