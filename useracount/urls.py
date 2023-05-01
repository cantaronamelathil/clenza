from django.urls import include,path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

    # path('admin/', admin.site.urls),
urlpatterns=[
    path('register/', views.UserRegistrationView.as_view()),
    path('login/',views.UserLogin.as_view()),
    path('profile/', views.ProfileView.as_view()),
    # path('workerprofile',views.WorkerprofileView.as_view()),
    path('logout/',views.LogoutView.as_view()),
    path('ClothOrderView/',views.ClothOrderView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ]