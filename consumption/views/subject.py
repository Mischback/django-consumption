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
