from django.urls import path
from .views import RegisterAPIView, LoginView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


urlpatterns = [
    path("jwt/create/",TokenObtainPairView.as_view(), name="jwt_create"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("jwt/verify/",TokenVerifyView.as_view(), name="token_verify"),
    path("registration/", RegisterAPIView.as_view(), name="register"),
    path("login/",LoginView.as_view(),name="login"),
]