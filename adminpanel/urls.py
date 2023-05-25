from django.urls import include,path
from .views import *
# path('admin/', admin.site.urls),
urlpatterns=[
    path('ClothOrderViewasAdmin/<str:booking_number>/', ClothOrderViewasAdmin.as_view()),
    path('AdminClothOrderView/<str:date>/', AdminClothOrderView.as_view()),]