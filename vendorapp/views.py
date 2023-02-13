from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.

from django.contrib.auth import  authenticate

from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import VendorRegistrationSerializer,VendorLoginSerializer
from useracount.serializers import UserRegistrationSerializer






def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
class VendorRegistrationView(APIView):
    def post(self, request):
        serializer = VendorRegistrationSerializer(data=request.data)    
        if serializer.is_valid():
            
            user = serializer.save()
            user.is_vendor=True
            user.save()
            return Response({'msg':'Vendor Registration Successful'},
            status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
class VendorLogin(APIView):
    def post(self, request, format=None):
        serializer = VendorLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            print(email)
            password = serializer.data.get('password')
            print(password)
            vendor = authenticate(email=email,password=password)
            print(vendor)
            if vendor:
                token = get_tokens_for_user(vendor)
                return Response({'token':token, 'msg':'Vendor Login Successful'})
            else:
                return Response({'msg':'Vendor Login Failed'})
