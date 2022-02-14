# SPDX-License-Identifier: MIT

"""App-specific URL configuration."""

# Django imports
from django.urls import path

# app imports
from consumption.views.record import (
    RecordCreateView,
    RecordDetailView,
    RecordUpdateView,
)
from consumption.views.resource import (
    ResourceCreateView,
    ResourceDeleteView,
    ResourceDetailView,
    ResourceUpdateView,
)
from consumption.views.subject import (
    SubjectCreateView,
    SubjectDeleteView,
    SubjectDetailView,
    SubjectListView,
    SubjectUpdateView,
)

app_name = "consumption"
"""Define an application namespace for reversing URLs.

See :djangodoc:`URL namespaces <topics/http/urls/#url-namespaces>`.
"""

urlpatterns = [
    # Subject-related URLs
    path("subject/create/", SubjectCreateView.as_view(), name="subject-create"),
    path("<int:subject_id>/", SubjectDetailView.as_view(), name="subject-detail"),
    path("subject/list/", SubjectListView.as_view(), name="subject-list"),
    path(
        "subject/<int:subject_id>/update/",
        SubjectUpdateView.as_view(),
        name="subject-update",
    ),
    path(
        "subject/<int:subject_id>/delete/",
        SubjectDeleteView.as_view(),
        name="subject-delete",
    ),
    # Resource-related URLs
    path("resource/create/", ResourceCreateView.as_view(), name="resource-create"),
    path(
        "resource/<int:resource_id>/",
        ResourceDetailView.as_view(),
        name="resource-detail",
    ),
    path(
        "resource/<int:resource_id>/update/",
        ResourceUpdateView.as_view(),
        name="resource-update",
    ),
    path(
        "resource/<int:resource_id>/delete/",
        ResourceDeleteView.as_view(),
        name="resource-delete",
    ),
    # Record-related URLs
    path("record/create/", RecordCreateView.as_view(), name="record-create"),
    path(
        "record/<int:record_id>/",
        RecordDetailView.as_view(),
        name="record-detail",
    ),
    path(
        "record/<int:record_id>/update/",
        RecordUpdateView.as_view(),
        name="record-update",
    ),
]
