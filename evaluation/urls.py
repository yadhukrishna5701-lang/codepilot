from django.urls import path
from evaluation.views import SumissionStartview,AnswerCreateView,SubmissionRetrieveView

urlpatterns={
    path("assessment/<int:pk>/submission/",SumissionStartview.as_view()),
    path("submission/<int:pk>/answer/",AnswerCreateView.as_view()),
    path("submission/<int:pk>/",SubmissionRetrieveView.as_view()),
}