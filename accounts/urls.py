from django.urls import path
from accounts.views import AdminCreateView
from accounts.views import StudentCreateViews


urlpatterns=[
    path("admin/register/",AdminCreateView.as_view()),
    path("student/register/",StudentCreateViews.as_view()),
]