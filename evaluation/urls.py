from django.urls import path
from evaluation.views import SumissionStartview,AnswerCreateView

urlpatterns={
    path("assessment/<int:pk>/submission/",SumissionStartview.as_view()),
    path("submission/<int:pk>/answer/",AnswerCreateView.as_view()),
    
}