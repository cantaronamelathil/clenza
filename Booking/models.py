from django.db import models
from django.conf import settings
from django.db.models import Q
from django.core.exceptions import ValidationError
from django.utils import timezone
from rest_framework import serializers
import datetime

# Create your models here.
class Appointment(models.Model):
    
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
    date = models.DateField()
    slot = models.IntegerField(choices=TIMESLOT_LIST)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cloth_no= models.IntegerField(blank=True,null=True)
    booking_number = models.CharField(max_length=100,blank=True,unique=True)
    @property
    def cost(self):
        return self.cloth_no * 30
   
    
    def __str__(self):
        return 'Time :{} , Slot: {} By : {}'.format(self.date, self.TIMESLOT_LIST[self.slot][1], self.user.username)
    
    @property
    def time(self):
        return self.TIMESLOT_LIST[self.timeslot][1]
    
    
    
  


class DispatchBooking(models.Model):
    
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
    dispatchdate = models.DateField()
    slot = models.IntegerField(choices=TIMESLOT_LIST,blank=True,null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    appointment=models.ForeignKey(Appointment, on_delete=models.CASCADE,null=True,blank=True, related_name='appointments')
    created_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    payment_id = models.CharField(max_length=255, blank=True, null=True)
    order_id = models.CharField(max_length=255, blank=True, null=True)
    refund = models.BooleanField(default=False)
    canceled = models.BooleanField(default=False)
    
    
    
    # def save(self, *args, **kwargs):
    #     if self.appointment:
    #         self.booking_number = self.appointment.booking_number
    #     super().save(*args, **kwargs)
    # @property
    # def booked_slot(self):
    #     return self.TIMESLOT_LIST[self.slot][1]
    
    
class ClothOrder(models.Model):
    order_status=(('Unassigned','Unassigned'),
                  ('Accepted','Accepted'),
                  ('Laundary','Laundary'),
                  ('Ironing','Ironing'),
                  ('Completed','Completed'))
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='appointmentclothes')
    order_status = models.CharField(max_length=20,choices=order_status,default='Unassigned')
    dispatch = models.ForeignKey(DispatchBooking,null=True,blank=True,on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
    booking_number = models.CharField(max_length=100,blank=True,null=True)
    # dispatch_date = serializers.SerializerMethodField()

    # def get_dispatch_date(self, obj):
    #     return obj.dispatch.dispatchdate if obj.dispatch else None
    
    dispatch_date = models.DateField(null=True, blank=True)
    # print(ClothOrder.id)
    def save(self, *args, **kwargs):
        if self.dispatch:
            self.dispatch_date = self.dispatch.dispatchdate
        super(ClothOrder, self).save(*args, **kwargs)