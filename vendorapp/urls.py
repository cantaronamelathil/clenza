from django.urls import include,path
from . import views

    # path('admin/', admin.site.urls),
urlpatterns=[
    path('register/', views.VendorRegistrationView.as_view()),
    path('login/',views.VendorLogin.as_view()),
    # path('profile/', views.ProfileView.as_view()),
    ]