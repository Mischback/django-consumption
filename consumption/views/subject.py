# SPDX-License-Identifier: MIT

"""Views related to the :class:`~consumption.models.subject.Subject` model."""

# Django imports
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy  # noqa: F401
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
    """Will use the template ``templates/consumption/subject_create.html``"""


class SubjectDetailView(generic.DetailView):
    """Provide the details of :class:`~consumption.models.subject.Subject` instances."""

    model = Subject
    """Required attribute, determining the model to work on."""

    context_object_name = "subject_instance"
    """Provide a semantic name for the built-in context."""

    pk_url_kwarg = "subject_id"
    """The keyword argument as provided in :source:`consumption.urls.py`."""
