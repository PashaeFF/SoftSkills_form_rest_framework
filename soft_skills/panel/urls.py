from django.urls import path
from .views import CreateForm, GetAllForm


urlpatterns = [
    path("forms/create_form/", CreateForm.as_view(), name="create_form"),
    path("forms/", GetAllForm.as_view(), name="forms_all"),
]