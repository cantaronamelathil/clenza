from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.

from django.contrib.auth import  authenticate

from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import VendorRegistrationSerializer,VendorLoginSerializer
from useracount.serializers import UserRegistrationSerializer
from rest_framework.permissions import IsAuthenticated
from Booking.models import ClothOrder
from Booking.serializers import Clothserializer





# def get_tokens_for_user(user):
#     refresh = RefreshToken.for_user(user)

#     return {
#         'refresh': str(refresh),
#         'access': str(refresh.access_token),
#     }
# class VendorRegistrationView(APIView):
#     def post(self, request):
#         serializer = VendorRegistrationSerializer(data=request.data)    
#         if serializer.is_valid():
            
#             user = serializer.save()
#             user.is_vendor=True
#             user.save()
#             return Response({'msg':'Vendor Registration Successful'},
#             status=status.HTTP_201_CREATED)
#         return Response(serializer.errors)
# class VendorLogin(APIView):
#     def post(self, request, format=None):
#         serializer = VendorLoginSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             email = serializer.data.get('email')
#             print(email)
#             password = serializer.data.get('password')
#             print(password)
#             vendor = authenticate(email=email,password=password)
#             print(vendor)
#             if vendor:
#                 token = get_tokens_for_user(vendor)
#                 return Response({'token':token, 'msg':'Vendor Login Successful'})
#             else:
#                 return Response({'msg':'Vendor Login Failed'})


# class ClothOrderAPIView(APIView):
#     permission_classes = [IsAuthenticated,Is_vendor]
#     serializer_class = Clothserializer

    # def get(self, request, format=None):
    #     user = request.user
    #     if user.is_authenticated and user.is_vendor:
    #         # Filter the objects by their order_status field
    #         queryset = ClothOrder.objects.filter(
    #             Q(order_status='Ironing') | Q(order_status='Laundry'),
    #             user=user
    #         )
    #     else:
    #         queryset = ClothOrder.objects.all()

    #     serializer = Clothserializer(queryset, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    
    # def post(self,request,format=None):
    #     user = request.user
    #     if user.is_autheticated and user.is_vendor:
    #         # user_name = 
              