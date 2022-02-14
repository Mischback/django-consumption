# SPDX-License-Identifier: MIT

"""Views related to the :class:`~consumption.models.subject.Subject` model."""

# Django imports
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

# app imports
from consumption.models.record import Record, RecordForm


class RecordCreateView(LoginRequiredMixin, generic.CreateView):
    """Generic class-based view to add :class:`~consumption.models.record.Record` objects.

    While this view requires a valid *login*, there is no check of permissions
    (as of now), meaning: every (authenticated) user is able to create
    :class:`~consumption.models.record.Record` objects.

    After successfully creating a new instance of
    :class:`~consumption.models.record.Record` the user will be redirected
    to the URL as provided by
    :meth:`Record.get_absolute_url() <consumption.models.record.Record.get_absolute_url>`.
    """

    model = Record
    """Required attribute, determining the model to work on."""

    form_class = RecordForm
    """Specify the form class to be used.

    It's either the ``fields`` attribute or ``form_class``. This ultimatively
    determines, which of the model's fields are rendered.

    This app uses the ``form_class``, because it also overwrites the template
    used for form rendering, see
    :class:`~consumption.models.record.RecordForm` for details.
    """

    template_name_suffix = "_create"
    """Uses the template ``templates/consumption/record_create.html``."""


class RecordDetailView(generic.DetailView):
    """Provide the details of :class:`~consumption.models.record.Record` instances.

    Uses the template ``templates/consumption/record_detail.html``.
    """

    model = Record
    """Required attribute, determining the model to work on."""

    context_object_name = "record_instance"
    """Provide a semantic name for the built-in context."""

    pk_url_kwarg = "record_id"
    """The keyword argument as provided in :mod:`consumption.urls`."""


class RecordUpdateView(LoginRequiredMixin, generic.UpdateView):
    """Generic class-based view to update :class:`~consumption.models.record.Record` objects.

    While this view requires a valid *login*, there is no check of permissions
    (as of now), meaning: every (authenticated) user is able to update any
    :class:`~consumption.models.record.Record` object.

    After successfully updating an instance of
    :class:`~consumption.models.record.Record` the user will be redirected
    to the URL as provided by
    :meth:`Record.get_absolute_url() <consumption.models.record.Record.get_absolute_url>`.
    """

    model = Record
    """Required attribute, determining the model to work on."""

    form_class = RecordForm
    """Specify the form class to be used.

    It's either the ``fields`` attribute or ``form_class``. This ultimatively
    determines, which of the model's fields are rendered.

    This app uses the ``form_class``, because it also overwrites the template
    used for form rendering, see
    :class:`~consumption.models.record.RecordForm` for details.
    """

    context_object_name = "record_instance"
    """Provide a semantic name for the built-in context."""

    pk_url_kwarg = "record_id"
    """The keyword argument as provided in :mod:`consumption.urls`."""

    template_name_suffix = "_update"
    """Uses the template ``templates/consumption/record_update.html``."""
