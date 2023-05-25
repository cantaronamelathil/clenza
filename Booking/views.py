from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
# Create your views here.
from rest_framework.response import Response
from .serializers import AppointmentSerializer,AvailableTimeSlotsSerializer,DispatchSerializer,SlotCancellationSerializer 
from .models import Appointment,DispatchBooking,ClothOrder
from rest_framework import status
import razorpay
import random
from django.conf import settings
from datetime import datetime, timedelta,date
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
# from datetime import date
from django.utils import timezone
class AppointmentView(APIView):
    
    def get(self,request,format=None):
        appointments = Appointment.objects.all()    
        serializers = AppointmentSerializer(appointments, many=True)  
        # serializers.save(user=request.user)
        return Response(serializers.data) 
    
    def post(self,request,format=None):
        # breakpoint()
        
        serializers= AppointmentSerializer(data=request.data,context={
        'request': request}) 
        if serializers.is_valid ():
            yr = int(date.today().strftime('%Y'))
            dt = int(date.today().strftime('%d'))
            mt = int(date.today().strftime('%m'))
            d = date(yr,mt,dt)
            current_date = d.strftime("%Y%m%d")
        
            booking_no = str(random.randint(1111111111,9999999999))
            
            print(request.user.id)
            booking_number = current_date + str(request.user.id)+ booking_no
            print(booking_no)
            # serializer. booking_number 
            # appointment.booking_number = booking_number
            if serializers.check(user=request.user):
                return Response({'the slot is already booked'})
            
            appointment=serializers.save(user=request.user, booking_number= booking_number)
            # booking = Appointment.objects.create(timeslot=timeslot,user=request.user,date=date)
            
            ClothOrder.objects.create(user=request.user,appointment=appointment)



            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return  Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    # hour must be after start hour!'}, status=status.HTTP_400_BAD_REQUEST)
    
    
class AvailableTimeSlots(APIView):
    
    def get(self,request,date,format=None):
        date_obj = datetime.strptime(date, '%Y-%m-%d').date()
        today = timezone.now().date()
        if date_obj == today:
            return Response({'message': 'Booking not possible on today\'s date'})
        elif date_obj < today:
            return Response({'message': 'Booking not possible on past date'})
        
        existing_appointments = Appointment.objects.filter(date=date)
        print(existing_appointments)
       
        available_slots = [i for i in range(9)]
        print(available_slots)
        for appointment in existing_appointments:
            print(appointment)
            available_slots.remove(appointment.slot)
        print(available_slots)
        serializer = AvailableTimeSlotsSerializer({'date': date, 'available_slots': available_slots,})
        return Response(serializer.data)
    
    
    
class DispatchView(APIView):
    
    def get(self,request,booking_number,format=None):
        # Calculate the date for dispatch, which is one week from the date of collection
        appointment=Appointment.objects.get(booking_number=booking_number)
        date=str(appointment.date)
        user=appointment.user
        print(date)
        dispatch_date = datetime.strptime(date, '%Y-%m-%d') + timedelta(days=7)
        print(dispatch_date)
        dispatch= DispatchBooking.objects.get_or_create(dispatchdate=dispatch_date,user=user,appointment=appointment)
        
        # Create a list of available time slots for the dispatch date
        existing_appointments = DispatchBooking.objects.filter(dispatchdate=dispatch_date)
        print(existing_appointments)
        available_slots = [i for i in range(9)]
        for item in existing_appointments:
            if item.slot:
                available_slots.remove(item.slot)
        
        # Create a response with the dispatch date and available time slots
        response_data = {
            'dispatch_date': dispatch_date.strftime('%Y-%m-%d'),
            'available_slots': available_slots,
        }
        return Response(response_data)    

    def put(self, request,booking_number,format=None):
        print("hi")
        # breakpoint()
        # Create a new dispatch instance and save it
        # print(request)
        # appointment_id = request.data["appoinment_id"]
        try:
            appointment=Appointment.objects.get(booking_number=booking_number)
        except Exception:
            return Response({'something'})
        print(appointment)
        try:
            dispatch=DispatchBooking.objects.get(appointment__booking_number=booking_number)
        except DispatchBooking.DoesNotExist:
            return Response({'message':'booking_number is not valid'})
        except DispatchBooking.MultipleObjectsReturned:
            return Response({'message':'already selected'})
        else:
            print(dispatch)
        # breakpoint()
        # dispatched= DispatchBooking.objects.get(id=id)
        
        # slot = dispatched.slot
        
        
        # print(dispatched)
        
        if dispatch.order_id:
            return Response({"message":'already slot selected'})
        
        serializer = DispatchSerializer(dispatch,data=request.data)
        if serializer.is_valid(raise_exception=True):
            # clothorder = ClothOrder.objects.get(slot=serializer.slot,user=request.user)
                slot =serializer.validated_data["slot"]
            # user = serializer.validated_data["user"]
                serializer.save()
                print(slot)
                print(serializer.data["user"])
                user=serializer.data["user"]
            
                # appointment = Appointment.objects.get(id=appointment_id)
                print(appointment)
                # dispatched= DispatchBooking.objects.get(id=id)
                clothorder = ClothOrder.objects.get(appointment=appointment)
                print(clothorder.dispatch)
                print(appointment)
                clothorder.dispatch=dispatch
        
                 
                razorpay_client = razorpay.Client(
                    auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET)
                )
                amount = appointment.cost * 100
                order_data = {
                    'amount':amount,
                    'currency':'INR',
                    'payment_capture' : 1
                }
                request.session['order_data'] = order_data
                print(request.session['order_data'])
                order = razorpay_client.order.create(order_data)
                print(f" the cost is {appointment.cost}")
            # breakpoint()
                dispatch.order_id = order['id']
                dispatch.save()
                clothorder.save()
                resp = {
                    "serializer.data":serializer.data,
                    "order_id" : order["id"]
                }
            
                return Response(resp, status=status.HTTP_201_CREATED)
        return Response('''serializer.errors''', status=status.HTTP_400_BAD_REQUEST)
    
    
        # appointment = Appointment.objects.get(booking_number=booking_number)
        # slot = request.data.get('slot')

     
    
    
class PaymentverifyAPIViews(APIView):
    # permission_classes =[IsAuthenticated]
       
       
       
    def post(self,request,*args,**kwargs):
        order_id= request.data.get('order_id')
        payment_id= request.data.get('payment_id')
        payment_signature=request.data.get('payment_signature')
        print(order_id,payment_id,payment_signature)
        try:
            dispatch=DispatchBooking.objects.get(order_id=order_id)
        except DispatchBooking.DoesNotExist:
            raise ValidationError('Invalid dispatch ID')
        
        razorpay_client = razorpay.Client(auth=(str(settings.RAZORPAY_KEY_ID),str(settings.RAZORPAY_KEY_SECRET)))
        # order_id = DispatchBooking.order_id
        
        
        
        context = {
            "razorpay_payment_id": payment_id,
            "razorpay_order_id": order_id,
            "razorpay_signature": payment_signature
        }

        try:
            razorpay_client.utility.verify_payment_signature(context)
        except Exception as e:
            raise ValidationError(str(e))
             # Mark the dispatch as paid and send a confirmation to the user
        dispatch.payment_id = payment_id
        dispatch.paid = True
        dispatch.save()
        # dispatch.slot.booked_tokens +=1
        # dispatch.slot.save()
        print(request.session.get('order_data'))
        order_details = request.session.get('order_data')
        del order_details['payment_capture']
        return Response({'status': 'success','amount':order_details})
 



class SlotCancellationView(APIView):
    def put(self, request, pk, format=None):
        try:
            dispatched = DispatchBooking.objects.get(pk=pk)
        except:
            return Response({"message":"invalid id"})
        # serializer = SlotCancellationSerializer(dispatched)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_200_OK)
        # return Response(seria  lizer.errors, status=status.HTTP_400_BAD_REQUEST)  
        dispatched.slot = None
        dispatched.save()
        return Response({"message":"succesfully cancelled"},status=status.HTTP_200_OK)
        