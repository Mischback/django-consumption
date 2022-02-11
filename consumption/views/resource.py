# SPDX-License-Identifier: MIT

"""Views related to the :class:`~consumption.models.subject.Subject` model."""

# Django imports
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy  # noqa: F401
from django.views import generic

# app imports
from consumption.models.resource import Resource, ResourceForm


class ResourceCreateView(LoginRequiredMixin, generic.CreateView):
    """Generic class-based view to add :class:`~consumption.models.resource.Resource` objects.

    While this view requires a valid *login*, there is no check of permissions
    (as of now), meaning: every (authenticated) user is able to create
    :class:`~consumption.models.resource.Resource` objects.

    After successfully creating a new instance of
    :class:`~consumption.models.resource.Resource` the user will be redirected
    to the URL as provided by
    :meth:`Resource.get_absolute_url() <consumption.models.resource.Resource.get_absolute_url>`.
    """

    model = Resource
    """Required attribute, determining the model to work on."""

    form_class = ResourceForm
    """Specify the form class to be used.

    It's either the ``fields`` attribute or ``form_class``. This ultimatively
    determines, which of the model's fields are rendered.

    This app uses the ``form_class``, because it also overwrites the template
    used for form rendering, see
    :class:`~consumption.models.resource.ResourceForm` for details.
    """

    template_name_suffix = "_create"
    """Uses the template ``templates/consumption/resource_create.html``."""
