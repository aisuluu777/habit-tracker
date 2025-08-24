from django.urls import path
from .views import RegisterUserView, RegisterCodeVerifyView
from rest_framework_simplejwt.views import TokenObtainPairView
urlpatterns = [
    path('register/', RegisterUserView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('code/verify/', RegisterCodeVerifyView.as_view())
]