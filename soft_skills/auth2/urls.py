from django.urls import path
from .views import RegisterAPIView, LoginView


urlpatterns = [
    path("registration/", RegisterAPIView.as_view(), name="register"),
    path("login/",LoginView.as_view(),name="login"),
]