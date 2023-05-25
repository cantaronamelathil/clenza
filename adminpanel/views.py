
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
from .serializers import AdminAppointmentsSerializer,ClothOrderSerializer

class ClothOrderViewasAdmin(APIView):
    permission_classes = [IsAuthenticated, Is_Admin]
    
    def put(self, request, booking_number, format=None):
        try:
            appointment = Appointment.objects.get(booking_number=booking_number)
            cloth_order = ClothOrder.objects.get(appointment=appointment)
        except Appointment.DoesNotExist:
            return Response({'status': 'Appointment not found.'}, status=status.HTTP_404_NOT_FOUND)
        except ClothOrder.DoesNotExist:
            return Response({'status': 'Order not found.'}, status=status.HTTP_404_NOT_FOUND)
    
        if cloth_order.order_status == 'Unassigned':
            cloth_order.order_status = "Accepted" 
            
        cloth_order.save()
        serializer = ClothOrderSerializer(cloth_order) 
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class  AdminClothOrderView(APIView):
    permission_classes =[IsAuthenticated,Is_Admin]
   
    def get(self, request, date):
        appointments = Appointment.objects.filter(date=date)
        serializer = AdminAppointmentsSerializer(appointments,many=True)
        result = []
        for item in appointments:
            clothorder = ClothOrder.objects.get(appointment=item)
            clothserializer = ClothOrderSerializer(clothorder,many=False)
            result.append(clothserializer.data)
        for item in range(len(serializer.data)):
            serializer.data[item]['order_status'] = result[item]['order_status']
        return Response(serializer.data)
