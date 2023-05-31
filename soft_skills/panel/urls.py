from django.urls import path
from .views import CreateForm


urlpatterns = [
    path("create_form/", CreateForm.as_view(), name="create_form"),
]