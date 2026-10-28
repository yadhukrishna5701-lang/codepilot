



    

from django.shortcuts import render,get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView,CreateAPIView

from exams.models import Assessment
from accounts.models import User
from exams.serializers import AssessmentSerializer
from exams.permissions import OwnerOnly

from datetime import datetime,time,timedelta

class AssessmentListView(ListAPIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = AssessmentSerializer
    queryset = Assessment.objects.all()

class AssessmentCreateView(CreateAPIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    serializer_class = AssessmentSerializer

    def perform_create(self, serializer):

        serializer.save(created_by=self.request.user)

class AssessmentRetrieveUpdateDeleteView(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [OwnerOnly]

    def get(self,request,pk=None):

        instance = get_object_or_404(Assessment,id=pk)

        self.check_object_permissions(request,instance)

        serializer_instance = AssessmentSerializer(instance)

        return Response(data=serializer_instance.data)

    def put(self,request,pk=None):

        form_data = request.data

        instance = get_object_or_404(Assessment,id=pk)

        self.check_object_permissions(request,instance)

        serializer_instance = AssessmentSerializer(data=form_data,instance=instance)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)

    def delete(self,request,pk=None):

        instance = get_object_or_404(Assessment,id=pk)

        self.check_object_permissions(request,instance)

        instance.delete()

        return Response({"message":"deleted"})

    