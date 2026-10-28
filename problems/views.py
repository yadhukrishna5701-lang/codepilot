from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions
from rest_framework.generics import RetrieveAPIView,UpdateAPIView,DestroyAPIView

from exams.models import Assessment
from problems.serializers import QuestionSeriazizer
from problems.models import Question

class QuestionCreateView(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def post(self,request,pk=None):

        assessment_id = pk
        assessment_object = Assessment.objects.get(id=assessment_id)

        form_data = request.data

        serializer_instance = QuestionSeriazizer(data=form_data)

        if serializer_instance.is_valid():

            serializer_instance.save(assessment=assessment_object,created_by=request.user)

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)

class QuestionRetriveupdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    serializer_class = QuestionSeriazizer
    queryset = Question.objects.all()
    