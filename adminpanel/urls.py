from django.urls import include,path
from .views import *
# path('admin/', admin.site.urls),
urlpatterns=[
    path('ClothOrderViewasAdmin/', ClothOrderViewasAdmin.as_view()),
    path('AdminClothOrderView/', AdminClothOrderView.as_view()),]