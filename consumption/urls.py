# SPDX-License-Identifier: MIT

"""App-specific URL configuration."""

# Django imports
from django.urls import path

# app imports
from consumption.views.subject import SubjectCreateView, SubjectDetailView

app_name = "consumption"
"""Define an application namespace for reversing URLs.

See :djangodoc:`URL namespaces <topics/http/urls/#url-namespaces>`.
"""

urlpatterns = [
    path("subject/create/", SubjectCreateView.as_view(), name="subject-create"),
    path("<int:subject_id>/", SubjectDetailView.as_view(), name="subject-detail"),
]
