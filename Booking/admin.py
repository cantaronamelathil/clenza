from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Appointment)

class AppointmentAdmin(admin.ModelAdmin):
    readonly_fields=('id',)
    # fields = ['user', 'date', 'slot']
class DispatchAdmin(admin.ModelAdmin):
    readonly_fields=('id',)  
    

admin.site.register(Appointment, AppointmentAdmin)

admin.site.register(DispatchBooking,DispatchAdmin)

admin.site.register(ClothOrder)