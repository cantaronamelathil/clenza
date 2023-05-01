from rest_framework import serializers
from Booking.models import ClothOrder
from useracount.models import Accounts

class ClothOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothOrder
        fields = ['order_status']
        
        
        
class WorkerprofileSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = Accounts
        fields = ['id','email']                