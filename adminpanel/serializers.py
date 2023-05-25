from rest_framework import serializers
from Booking.models import Appointment,ClothOrder

class AdminAppointmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('booking_number', 'cloth_no')




class ClothOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothOrder
        fields = ['order_status']