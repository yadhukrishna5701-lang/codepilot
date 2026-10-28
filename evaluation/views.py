from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework import permissions,authentication
from evaluation.permission import IsStudentuser
from evaluation.models import Submission
from exams.models import Assessment
from evaluation.serializers import SubmissionSerializer,AnswerSerializer
from rest_framework.response import Response
# Create your views here.

class SumissionStartview(APIView):

   permission_classes=[IsStudentuser]
   authentication_classes=[authentication.TokenAuthentication]

   def post(self,request,pk=None):
       assessment_id = pk
       assessment_object = get_object_or_404(Assessment,id=assessment_id)

       instance = Submission.objects.create(assessment = assessment_object,student = request.user)

       serializer_instance = SubmissionSerializer(instance)

       return Response (data=serializer_instance.data)


      
class AnswerCreateView(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsStudentuser]

    def post(self,request,pk = None):

        submission_id = pk

        submission_object = get_object_or_404(Submission,id = submission_id)

        form_data = request.data

        serializer_instance = AnswerSerializer(data = form_data)

        if serializer_instance.is_valid():

            serializer_instance.save(submission = submission_object)

            return Response(data = serializer_instance.data)
        
        else:

            return Response(data = serializer_instance.errors)
