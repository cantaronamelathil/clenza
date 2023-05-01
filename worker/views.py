from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .permissions import permissions
from rest_framework.permissions import IsAuthenticated,AllowAny
# from .permissions import Is_WORKER # Import the custom permission class
from Booking.models import ClothOrder
from .serializers import ClothOrderSerializer,WorkerprofileSerializer
from .permissions import Is_Worker

class WorkerprofileView(APIView):
    permission_classes = [IsAuthenticated] 
    
    def get(self,request, format=None):
        serializer = WorkerprofileSerializer(request.user)
        return  Response(serializer.data)

class ClothOrderUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated,Is_Worker]

    def put(self, request, pk, format=None):
        try:
            cloth_order = ClothOrder.objects.get(pk=pk)
           
        except ClothOrder.DoesNotExist:
            return Response({'status': 'Order not found.'}, status=status.HTTP_404_NOT_FOUND)

        print(cloth_order.order_status)
        if cloth_order.order_status == 'Ironing':
            cloth_order.order_status = "Completed"
        elif cloth_order.order_status == 'Laundary':
            cloth_order.order_status = 'Ironing'
        elif cloth_order.order_status == 'Accepted':
            cloth_order.order_status = 'Laundary'

        cloth_order.save()
        serializer = ClothOrderSerializer(cloth_order) 
        return Response(serializer.data, status=status.HTTP_200_OK)

        # return Response({'status': 'Order status cannot be updated.'},status=status.HTTP_400_BAD_REQUEST)