from rest_framework import serializers
from Booking.models import Appointment



class AppointmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Appointment
        fields = ['date', 'slot', 'user']
        # extra_kwargs = {'password': {'write_only': True}}
