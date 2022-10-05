from pyexpat import model
from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from Accounts.serializer import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework import filters
from rest_framework import generics
# Create your views here.

class RegisterAPI(APIView):
    def post(self, request):
        data = request.data
        if len(data['phone_number']) > 10:
            return Response({
                'status' : 400,
                'message' : 'Mobile Number Not valid',
            })
        serializer = UserSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status' : 200,
                'message' : 'registration Succesfull',
                'data': serializer.data
            })
        return Response({
            'status' : 400,
            'message' : 'something went wrong',
            'data': serializer.errors
        })

class UserListAPI(APIView):
    def get(self, request):
        User = get_user_model()
        model = User.objects.all()
        serializer = UserSerializer(model, many = True)
        return Response({
            'status' : 200,
            'message' : 'all User',
            'data': serializer.data
            })

class EmailSearchAPIView(generics.ListCreateAPIView):
    User = get_user_model()
    search_fields = ['email']
    filter_backends = (filters.SearchFilter,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EmailSearchAPIView(generics.ListCreateAPIView):
    User = get_user_model()
    search_fields = ['email']
    filter_backends = (filters.SearchFilter,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class NameSearchAPIView(generics.ListCreateAPIView):
    User = get_user_model()
    search_fields = ['first_name', 'last_name']
    filter_backends = (filters.SearchFilter,)
    queryset = User.objects.all().order_by('-date_joined') 
    serializer_class = UserSerializer