from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from exams.views import AssessmentListView,AssessmentCreateView,AssessmentRetrieveUpdateDeleteView

urlpatterns=[
    path("token/",ObtainAuthToken.as_view()),
    path("all/",AssessmentListView.as_view()),
    path("add/",AssessmentCreateView.as_view()),
    path("<int:pk>/",AssessmentRetrieveUpdateDeleteView.as_view()),
]