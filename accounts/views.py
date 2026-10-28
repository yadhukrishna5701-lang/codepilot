from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.serializers import UsersSerializer
from accounts.models import User



class AdminCreateView(APIView):

    def post(self,request):

        from_data = request.data

        serializer_instance = UsersSerializer(data = from_data)

        if serializer_instance.is_valid():
            cleanded_data = serializer_instance.validated_data
            instance = User.objects.create_superuser(role="admin",**cleanded_data)
            serializer_instance=UsersSerializer(instance)

            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)


class StudentCreateViews(APIView):

    def post(self,request):

        form_data=request.data
        serializer_instance = UsersSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleanded_data = serializer_instance.validated_data
            instance = User.objects.create_user(role="student",**cleanded_data)
            serializer_instance = UsersSerializer(instance)

            return Response(data=serializer_instance.data)

        else:
            return Response(data=serializer_instance.errors)