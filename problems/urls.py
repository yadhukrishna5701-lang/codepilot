from django.urls import path
from problems.views import QuestionCreateView,QuestionRetriveupdateDeleteView

urlpatterns=[
    path("assessment/<int:pk>/question/",QuestionCreateView.as_view()),
    path("assessment/question/<int:pk>/",QuestionRetriveupdateDeleteView.as_view()),

]