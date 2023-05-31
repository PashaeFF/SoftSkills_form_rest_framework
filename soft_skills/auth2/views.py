from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer
from drf_yasg.utils import swagger_auto_schema


class RegisterAPIView(GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = []

    @swagger_auto_schema(operation_id="Registration", tags=['Authentication'], request_body=RegisterSerializer)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class LoginView(APIView):
    permission_classes = []

    def post(self, request: Request):
        email = request.data.get('email')
        password = request.data.get('password')

        user=authenticate(email=email,password=password)
        if user is not None:
            response ={
                'message':'Login Successfull',
                'token':user.auth_token.key
            }
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response(data={'message':'Invalid email or password'}, status=status.HTTP_200_OK)


    def get(self, request: Request):
        content = {
            "user":str(request.user),
            "auth":str(request.auth)
        }
        return Response(data=content, status=status.HTTP_200_OK)
