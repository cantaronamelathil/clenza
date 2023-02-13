from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
# Create your views here.


class BookingView(APIView):
    def post(self,request,format=None):
        