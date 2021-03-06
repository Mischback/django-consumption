# SPDX-License-Identifier: MIT

"""Views related to the :class:`~consumption.models.subject.Subject` model."""

# Django imports
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

# app imports
from consumption.models.subject import Subject, SubjectForm


class SubjectCreateView(LoginRequiredMixin, generic.CreateView):
    """Generic class-based view to add :class:`~consumption.models.subject.Subject` objects.

    While this view requires a valid *login*, there is no check of permissions
    (as of now), meaning: every (authenticated) user is able to create
    :class:`~consumption.models.subject.Subject` objects.

    After successfully creating a new instance of
    :class:`~consumption.models.subject.Subject` the user will be redirected
    to the URL as provided by
    :meth:`Subject.get_absolute_url() <consumption.models.subject.Subject.get_absolute_url>`.
    """

    model = Subject
    """Required attribute, determining the model to work on."""

    form_class = SubjectForm
    """Specify the form class to be used.

    It's either the ``fields`` attribute or ``form_class``. This ultimatively
    determines, which of the model's fields are rendered.

    This app uses the ``form_class``, because it also overwrites the template
    used for form rendering, see
    :class:`~consumption.models.subject.SubjectForm` for details.
    """

    template_name_suffix = "_create"
    """Uses the template ``templates/consumption/subject_create.html``."""


class SubjectDetailView(generic.DetailView):
    """Provide the details of :class:`~consumption.models.subject.Subject` instances.

    Uses the template ``templates/consumption/subject_detail.html``.
    """

    model = Subject
    """Required attribute, determining the model to work on."""

    context_object_name = "subject_instance"
    """Provide a semantic name for the built-in context."""

    pk_url_kwarg = "subject_id"
    """The keyword argument as provided in :mod:`consumption.urls`."""


class SubjectListView(generic.ListView):
    """Provide a list of :class:`~consumption.models.subject.Subject` instances.

    Uses the template ``templates/consumption/subject_list.html``.
    """

    model = Subject
    """Required attribute, determining the model to work on."""

    context_object_name = "subject_list"
    """Provide a semantic name for the built-in context."""


class SubjectUpdateView(LoginRequiredMixin, generic.UpdateView):
    """Generic class-based view to update :class:`~consumption.models.subject.Subject` objects.

    While this view requires a valid *login*, there is no check of permissions
    (as of now), meaning: every (authenticated) user is able to update any
    :class:`~consumption.models.subject.Subject` object.

    After successfully updating an instance of
    :class:`~consumption.models.subject.Subject` the user will be redirected
    to the URL as provided by
    :meth:`Subject.get_absolute_url() <consumption.models.subject.Subject.get_absolute_url>`.
    """

    model = Subject
    """Required attribute, determining the model to work on."""

    form_class = SubjectForm
    """Specify the form class to be used.

    It's either the ``fields`` attribute or ``form_class``. This ultimatively
    determines, which of the model's fields are rendered.

    This app uses the ``form_class``, because it also overwrites the template
    used for form rendering, see
    :class:`~consumption.models.subject.SubjectForm` for details.
    """

    context_object_name = "subject_instance"
    """Provide a semantic name for the built-in context."""

    pk_url_kwarg = "subject_id"
    """The keyword argument as provided in :mod:`consumption.urls`."""

    template_name_suffix = "_update"
    """Uses the template ``templates/consumption/subject_update.html``."""


class SubjectDeleteView(LoginRequiredMixin, generic.DeleteView):
    """Generic class-based view to delete :class:`~consumption.models.subject.Subject` objects.

    While this view requires a valid *login*, there is no check of permissions
    (as of now), meaning: every (authenticated) user is able to delete any
    :class:`~consumption.models.subject.Subject` object.

    After successfully deleting an instance of
    :class:`~consumption.models.subject.Subject` the user will be redirected
    to the URL of :class:`~consumption.views.subject.SubjectListView`, as
    specified in :mod:`consumption.urls`.

    Uses the template ``templates/consumption/subject_confirm_delete.html``.
    """

    model = Subject
    """Required attribute, determining the model to work on."""

    context_object_name = "subject_instance"
    """Provide a semantic name for the built-in context."""

    pk_url_kwarg = "subject_id"
    """The keyword argument as provided in :mod:`consumption.urls`."""

    success_url = reverse_lazy("consumption:subject-list")
    """The URL to redirect to after successfully deleting the instance."""
