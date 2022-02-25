# SPDX-License-Identifier: MIT

"""Views related to the :class:`~consumption.models.resource.Resource` model."""

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

    def get_queryset(self):
        """Optimize database queries.

        Override to the default implementation of ``get_queryset()`` to
        select the referenced instance of
        :class:`~consumption.models.subject.Subject` (referenced by
        :attr:`Resource.subject <consumption.models.resource.Resource.subject>`)
        and prefetch all associated instances of
        :class:`~consumption.models.record.Record` (that is: all instances of
        :class:`~consumption.models.record.Record` that reference this instance
        of :class:`~consumption.models.resource.Resource` by their
        :attr:`~consumption.models.record.Record.resource` attribute).

        Warning
        -------
        This method does only modify / extend / prepare the actual database
        queries, it does not provide the resulting objects in the rendering
        context for the template (actually the
        :class:`~consumption.models.subject.Subject` instance will be easily
        accessible by using ``resource_instance.subject`` in the template).

        See
        :meth:`~consumption.views.resource.ResourceDetailView.get_context_data`
        for that.
        """
        return (
            super()
            .get_queryset()
            .select_related("subject")
            .prefetch_related("record_set")
        )

    def get_context_data(self, **kwargs):
        """Add a list of related ``Record`` instances to the context.

        :meth:`~consumption.views.resource.ResourceDetailView.get_queryset`
        will optimize the database access, but the list of
        :class:`~consumption.models.record.Record` instances must still be
        added to the rendering context.
        """
        context = super().get_context_data(**kwargs)

        if self.object:
            context["records"] = self.object.record_set.all()

        return context


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

    def get_success_url(self):  # pragma: nocover
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
