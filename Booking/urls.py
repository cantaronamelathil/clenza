from django.urls import include,path
from .views import *
# path('admin/', admin.site.urls),
urlpatterns=[
    path('AppointmentView/', AppointmentView.as_view()),
    path('AvailableTimeSlots/<str:date>/', AvailableTimeSlots.as_view(), name='AvailableTimeSlots'),
    path('DispatchView/<int:id>/', DispatchView.as_view()),
    path('SlotCancellationView/<int:pk>/', SlotCancellationView.as_view()),
    path('PaymentverifyAPIViews/', PaymentverifyAPIViews.as_view()),
    ]