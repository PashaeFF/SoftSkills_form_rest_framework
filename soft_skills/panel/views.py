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
from .models import Form
from .serializers import FormsAllSerializer
from auth2.models import User


class CreateForm(GenericAPIView):
    serializer_class = FormSerializer
    permission_classes = []

    @swagger_auto_schema(operation_id="Creat Skills Form", tags=['Forms'], request_body=FormSerializer)
    def post(self, request):
        current_user = request.user.id
        if current_user:
            user = User.objects.get(id=current_user)
            if user:
                form = request.data
                check_value_errors = check_values(form.get("form_name"),form.get("values"))
                if not check_value_errors:
                    new_form = Form.objects.create(owner_id=user,
                                                form_name=form['form_name'],
                                                values=form['values'])
                    new_form.save()
                    return Response({'success':'Form added'}, status=status.HTTP_201_CREATED)
                return Response({'error':check_value_errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'Not authenticated'}, status=status.HTTP_400_BAD_REQUEST)
        

class GetAllForm(GenericAPIView):
    permission_classes = []

    @swagger_auto_schema(operation_id="Get Forms", tags=['Forms'])
    def get(self, request):
        current_user = request.user.id
        if current_user:
            user = User.objects.filter(id=current_user).first()
            if user:
                forms = Form.objects.all()
                context = {
                            'title':'Forms',
                        }
                serializer_class = FormsAllSerializer(forms, many=True)
                return Response({"context":context, "data":serializer_class.data}, status=status.HTTP_200_OK)
        return Response({'error':'Not authenticated'}, status=status.HTTP_400_BAD_REQUEST)