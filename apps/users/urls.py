from django.urls import path
from .views import RegisterUserView, RegisterCodeVerifyView, GoogleLoginView, GoogleCallbackView
from rest_framework_simplejwt.views import TokenObtainPairView
urlpatterns = [
    path('register/', RegisterUserView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('code/verify/', RegisterCodeVerifyView.as_view()),
    path('google/login/', GoogleLoginView.as_view()),
    path('token/', GoogleCallbackView.as_view())
]