from django.shortcuts import render
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
# from useracount.serializers import authenticate
from django.contrib.auth import  authenticate
from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import UserRegistrationSerializer, UserLoginSerializer,UserprofileSerializer
from Booking.models import  ClothOrder,DispatchBooking,Appointment
from Booking.serializers import Clothserializer
from useracount.models import Accounts

# Create your views here.
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserRegistrationView(APIView):  
#    permission_classes=[IsAuthenticated]
   
   def post(self,request,format=None):
       serializer= UserRegistrationSerializer(data=request.data)    
       if serializer.is_valid(raise_exception=True):
           user = serializer.save()
           return Response({'msg':'Registration succesful'},
           status=status.HTTP_201_CREATED)
       return Response(serializer.errors)
    
# Create your views here.
class UserLogin(APIView):

    def post(self, request , format=None):
        serializer = UserLoginSerializer(data= request.data)
        # if not user:
        #     print("Authentication failed: " + str(authenticate.errors))
        if serializer.is_valid(raise_exception = True):
            email = serializer.data.get('email')
            # print(email)
            password = serializer.data.get('password')
            # print(password)
            user = authenticate(email=email,password=password)
            # print(user)
            # if not user:
            #     print("Authentication failed: " + str(authenticate.errors))
            if user:
                # return Response({'msg':'Login Success'},status=status.HTTP_200_OK)
                if user.role=="CUSTOMER":
                    tokens= get_tokens_for_user(user)
                    return Response({"message":
                    "customerlogin successful","Tokens":tokens},status=status.HTTP_202_ACCEPTED)
                elif user.role=="VENDOR":
                    tokens=get_tokens_for_user(user)
                    return Response({"message":"vendor login succesful","TOKENS":tokens},status=status.HTTP_202_ACCEPTED)
                elif user.role =="ADMIN":
                    tokens=get_tokens_for_user(user)
                    return Response({"message":"Admin login succesful","Tokens":tokens},status=status.HTTP_202_ACCEPTED)
                elif user.role =="WORKER":
                    tokens=get_tokens_for_user(user)
                    return Response({"message":"Worker login succesful","Tokens":tokens},status=status.HTTP_202_ACCEPTED)
            else:
                return Response({"message":'Login Failed'},status=status.HTTP_202_ACCEPTED)
            

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        serializer= UserprofileSerializer(request.user)
        print(request.user)
        return Response(serializer.data)

class LogoutView(APIView):
    def post(self, request):
        refresh_token = request.data.get('refresh_token')
        if refresh_token:
            try:
                token = RefreshToken(refresh_token)
                token.blacklist()
                return Response({'message': 'Logout successful.'})
            except Exception as e:
                return Response({'error': str(e)}, status=400)
        else:
            return Response({'error': 'Refresh token is required.'}, status=400)    
        
# class ClothOrderView(APIView):
#     def get(self,request,format =None):
#         user = request.user
#         # clothorder = ClothOrder.objects.filter(user=user)
#         # dispatch_dates = DispatchBooking.objects.values('id', 'dispatchdate')
#         # dispatch_dates_dict = {str(d['id']): d['dispatchdate'] for d in dispatch_dates}
#         clothorder= ClothOrder.objects.filter(user=user).prefetch_related('dispatch')
#         serializer = Clothserializer(clothorder, many = True)

#         return Response(serializer.data)



class UserClothOrderView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        user = Accounts.objects.get(email = request.user)
        try:
            booking_object = Appointment.objects.get(user=user)
        except Appointment.DoesNotExist:
            return Response({'error':'User not valid'})
        else:
            try:
                dispatch_object = DispatchBooking.objects.get(user=user)
            except DispatchBooking.DoesNotExist:
                result = {
                    'booking_date':booking_object.date,
                    'booking_number':booking_object.booking_number,
                    'message':'dispatch is not complete'
                }
                return Response(result)
            else:
                result = {
                    'booking_date':booking_object.date,
                    'booking_number':booking_object.booking_number,
                    'cloth_number':booking_object.cloth_no,
                    'dispatch_date':dispatch_object.dispatchdate,
                    'dispatch_slot':dispatch_object.slot,
                }
                return Response(result)