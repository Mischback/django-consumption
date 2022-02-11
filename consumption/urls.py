# SPDX-License-Identifier: MIT

"""App-specific URL configuration."""

# Django imports
from django.urls import path

# app imports
from consumption.views.resource import ResourceCreateView
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
    path("resource/create/", ResourceCreateView.as_view(), name="resource-create"),
]
