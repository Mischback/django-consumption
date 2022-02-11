# SPDX-License-Identifier: MIT

"""Views related to the :class:`~consumption.models.subject.Subject` model."""

# Django imports
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
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


class ResourceDetailView(generic.DetailView):
    """Provide the details of :class:`~consumption.models.resource.Resource` instances.

    Uses the template ``templates/consumption/resource_detail.html``.
    """

    model = Resource
    """Required attribute, determining the model to work on."""

    context_object_name = "resource_instance"
    """Provide a semantic name for the built-in context."""

    pk_url_kwarg = "resource_id"
    """The keyword argument as provided in :mod:`consumption.urls`."""


class ResourceUpdateView(LoginRequiredMixin, generic.UpdateView):
    """Generic class-based view to update :class:`~consumption.models.resource.Resource` objects.

    While this view requires a valid *login*, there is no check of permissions
    (as of now), meaning: every (authenticated) user is able to update any
    :class:`~consumption.models.resource.Resource` object.

    After successfully updating an instance of
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

    context_object_name = "resource_instance"
    """Provide a semantic name for the built-in context."""

    pk_url_kwarg = "resource_id"
    """The keyword argument as provided in :mod:`consumption.urls`."""

    template_name_suffix = "_update"
    """Uses the template ``templates/consumption/resource_update.html``."""


class ResourceDeleteView(LoginRequiredMixin, generic.DeleteView):
    """Generic class-based view to delete :class:`~consumption.models.resource.Resource` objects.

    While this view requires a valid *login*, there is no check of permissions
    (as of now), meaning: every (authenticated) user is able to delete any
    :class:`~consumption.models.resource.Resource` object.

    After successfully deleting an instance of
    :class:`~consumption.models.resource.Resource` the user will be redirected
    to the URL of :class:`~consumption.views.subject.SubjectDetailView` of the
    :class:`~consumption.models.subject.Subject` instance the ``Resource`` was
    associated with.

    Uses the template ``templates/consumption/resource_confirm_delete.html``.
    """

    model = Resource
    """Required attribute, determining the model to work on."""

    context_object_name = "resource_instance"
    """Provide a semantic name for the built-in context."""

    pk_url_kwarg = "resource_id"
    """The keyword argument as provided in :mod:`consumption.urls`."""

    def get_success_url(self):
        """Determine the URL for redirecting after successful deletion.

        This has to be done dynamically with a method instead of statically
        with the ``success_url`` attribute, because the user should be
        redirected to the *parent* :class:`~consumption.models.subject.Subject`
        instance.
        """
        subject = self.object.subject
        return reverse_lazy(
            "consumption:subject-detail", kwargs={"subject_id": subject.id}
        )
