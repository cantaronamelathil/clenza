from django.urls import include,path
from . import views

    # path('admin/', admin.site.urls),
urlpatterns=[
    path('register/', views.UserRegistrationView.as_view()),
    path('login/',views.UserLogin.as_view()),
    path('profile/', views.ProfileView.as_view()),
    ]