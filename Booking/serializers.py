from rest_framework import serializers
from Booking.models import Appointment, DispatchBooking,ClothOrder
from django.core.exceptions import ValidationError
from django.db.models import Q
from datetime import date
from .models import Appointment
from useracount.models import Accounts
class AppointmentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    cloth_no = serializers.IntegerField(required=True )
    booking_number =serializers.CharField(required=False)
    class Meta:
        model = Appointment
        fields = ['date', 'slot', 'time', 'user','cloth_no','booking_number']
        # extra_kwargs = {'password': {'write_only': True}}
     
    # def create(self, validated_data):
          
    def validate_date(self,value):
        # Check if the date is in the past
        if value < date.today():
            raise serializers.ValidationError("Appointment date cannot be in the past.")
        return value  
    


    # def save(self, **kwargs):
    #     appoiment_object = Appointment.objects.get_or_create(
    #     date=self.data.get('date'),
    #     slot=self.data.get('slot'),
    #     cloth_no=self.data.get('cloth_no'),
    #     )
    #     appoiment_object[0].user =kwargs.get('user')
    #     appoiment_object[0].booking_number = kwargs.get('booking_number')
    #     appoiment_object[0].save()
    #     return [appoiment_object[0], appoiment_object[0].user]
    

    def check(self, **kwargs):
        user = Accounts.objects.get(email=kwargs.get('user'))
        print(type(user))
        print(self.validated_data.get('date'))
        
        try:
            appointment = Appointment.objects.get(date=self.validated_data.get('date'))
            
        except Exception:
            return False
        else:
            print(appointment,type(appointment))
            return True
        
        
    def validate(self, data):
        # Check if the time slot is available for the given date
        date = data.get('date')
        slot = data.get('slot')
        
        user = data.get('user')
     
        # Queryset that finds all clashing timeslots with the same date
        queryset = Appointment.objects.filter(date=date, user=user)
        
        # breakpoint()
        
        # if self.instance:
            # Exclude the current instance from the queryset if it is being updated
            # queryset = queryset.exclude(pk=self.instance.pk)
        
        if queryset.exists():
            # Raise a validation error if there's a clash
            raise ValidationError('An existing timeslot clashes with the given one!')
        
        return data
        



class AvailableTimeSlotsSerializer(serializers.ModelSerializer):
    TIMESLOT_LIST = (
        (0, '09:00 - 09:30 AM'),
        (1, '10:00 - 10:30 AM'),
        (2, '11:00 - 11:30 AM'), 
        (3, '12:00 - 12:30 PM'),
        (4, '01:00 - 01:30 PM'),
        (5, '14:00 - 14:30 PM'),
        (6, '15:00 - 15:30 PM'),
        (7, '16:00 - 16:30 PM'),
        (8, '17:00 - 17:30 PM'),
    )
    
    available_slots = serializers.SerializerMethodField()

    class Meta:
        model = Appointment
        fields = ['date', 'available_slots']
        
    def get_available_slots(self, obj):
        # breakpoint()
        taken_slots = Appointment.objects.filter(date=obj.get("date")).values_list('slot', flat=True)
        # all_slots = [i for i in range(9)]
        available_slots = [f"Slot {data[0]}: {data[1]}" for data in self.TIMESLOT_LIST if data[0] not in taken_slots]
        return available_slots
  
    
class DispatchSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    dispatchdate = serializers.DateField(read_only= True)
    class Meta:
        model = DispatchBooking
        fields = ['slot','user','dispatchdate']
        
    
  
    
    # def update(self, instance, validated_data):
    #     # breakpoint()
    #     return super().update(instance, validated_data)
    

    # def validate(self, data):
        # Ensure that delivery date is one week from the collection date
        # collection_date = data['collection_date']
        # delivery_date = data['delivery_date']
        # if (delivery_date - collection_date).days != 7:
        #     raise serializers.ValidationError('Delivery date must be one week from collection date')
        # # return data
        
        
        
        # dispatchdate = data.get('dispatchdate ')
        # slot = data.get('slot')
        # request = self.context.get('request', None)
        # user= request.user
        # queryset = DispatchBooking.objects.filter(dispatchdate=dispatchdate , user=user)
        # if queryset.exists():
        #     raise ValidationError('An existing timeslot clashes with the given one!')
        
        # return data
        
        
        
        
class SlotCancellationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DispatchBooking
        fields = ['id', 'slot']
    
    def update(self, instance, validated_data):
        instance.slot = None
        instance.save()
        return instance      
    
# class Clothserializer(serializers.ModelSerializer):
#     class Meta:
#         model = ClothOrder
#         fields = 

# class Clothserializer(serializers.ModelSerializer):
#     user_name = serializers.SerializerMethodField()
#     # dispatch_date = serializers.DateField(source='dispatch.dispatchdate', read_only=True)

#     class Meta:
#         model = ClothOrder
#         fields = ['id', 'order_status', 'appointment', 'user_name','dispatch']

#     def get_user_name(self, obj):
#         return obj.user.username



# class Clothserializer(serializers.ModelSerializer):
#     user_name = serializers.SerializerMethodField()
#     dispatch_date = serializers.DateField(read_only=True)

#     # def __init__(self, *args, **kwargs):
#     #     dispatch_dates = kwargs.pop('dispatch_dates', None)
#     #     super().__init__(*args, **kwargs)
#     #     if dispatch_dates is not None:
#     #         self.fields['dispatch_date'] = serializers.SerializerMethodField()
#     #         self.dispatch_dates = dict(dispatch_dates)

#     def get_dispatch_date(self, obj):
#         # return obj.dispatch.dispatchdate
#         dispatch = obj.dispatch
#         if dispatch is not None:
#             return dispatch.dispatchdate
#         else:
#             return None
    
#     def get_user_name(self, obj):
#         return obj.user.username
#     class Meta:
#         model = ClothOrder
#         fields = ['id', 'order_status', 'appointment', 'user_name', 'dispatch','dispatch_date']
        
        
class Clothserializer(serializers.ModelSerializer):
        user_name = serializers.SerializerMethodField()
        dispatch = DispatchSerializer(read_only =True)
        # breakpoint()
        dispatch_date = serializers.DateField(source='dispatchBooking.dispatchdate',read_only=True)
        print(dispatch_date)
        # print(dispatch_date)
        # def get_dispatch_date(self, obj):
        #     dispatch = obj.dispatch
        #     if dispatch is not None:
        #         return dispatch.dispatchdate
        #     else:
        #         return None

        def get_user_name(self, obj):
            return obj.user.username

        class Meta:
            model = ClothOrder
            fields = ['id', 'order_status', 'appointment', 'user_name','dispatch', 'dispatch_date']
