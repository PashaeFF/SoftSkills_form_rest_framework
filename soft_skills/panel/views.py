from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .serializers import FormSerializer
from rest_framework.views import APIView
from rest_framework.decorators import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .utils.helper import check_values


class CreateForm(GenericAPIView):
    serializer_class = FormSerializer
    permission_classes = []

    @swagger_auto_schema(operation_id="Creat Skills Form", tags=['Forms'], request_body=FormSerializer)
    def post(self, request):
        form = request.data
        check_value_errors = check_values(form.get("form_name"),form.get("values"))
        if check_value_errors:
            return {'error':check_value_errors}

        return Response("message", status=status.HTTP_400_BAD_REQUEST)
    