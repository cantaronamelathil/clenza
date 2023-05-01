from django.urls import include,path
from . import views

    # path('admin/', admin.site.urls),
urlpatterns=[
    path('WorkerprofileView/', views.WorkerprofileView.as_view()),
    path('ClothOrderUpdateAPIView/<int:pk>',views.ClothOrderUpdateAPIView.as_view()),
    # path('profile/', views.ProfileView.as_view()),
    ]