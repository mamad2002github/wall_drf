from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from acconts.serializers import UserSerializer


# Create your views here.


class UserApiView(APIView):
    def get(self, request):
       user = request.user
       serializer = UserSerializer(user)
       return Response(serializer.data,status=status.HTTP_200_OK)