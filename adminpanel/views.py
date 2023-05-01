from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
# Create your views here.
from Booking.models import ClothOrder
from .permissions import Is_Admin
from rest_framework import status
from rest_framework.response import Response
from worker.serializers import ClothOrderSerializer
from Booking.models import Appointment
from Booking.serializers import AppointmentSerializer
class ClothOrderViewasAdmin(APIView):
    permission_classes = [IsAuthenticated,Is_Admin]
    
    def put(self,request,pk,format=None):
        try:
            cloth_order  = ClothOrder.objects.gets(pk=pk)
        
        except ClothOrder.DoesNotExist:
            return Response({'status':'Order not found.'},status=status.HTTP_404_NOT_FOUND)
    
        if cloth_order.order_status == 'Unassigned':
            cloth_order.order_status = "Accepted" 
            
        cloth_order.save()
        serializer = ClothOrderSerializer(cloth_order) 
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class  AdminClothOrderView(APIView):
    permission_classes =[IsAuthenticated,Is_Admin]
    def get(self,reuest,pk,format=None):
        appointments=Appointment.objects.filter(pk=pk)
        print(appointments)
        serializer=AppointmentSerializer(appointments,many=True)
        
        return Response(serializer.data)

