from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .serializers import FormSerializer
from rest_framework.decorators import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .utils.helper import check_values, check_fill_form_key_and_values, add_filled_form
from .models import Form, FilledForm
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
    

class GetForm(APIView):
    permission_classes = []

    @swagger_auto_schema(operation_id="Get Form", tags=['Forms'])
    def get(self,request,pk):
        current_user = request.user.id
        if current_user:
            user = User.objects.filter(id=current_user).first()
            if user:
                form_pk = Form.objects.filter(id=pk).first()
                if form_pk:
                    return Response({'title':form_pk.form_name,
                                'values':form_pk.values}, status=status.HTTP_200_OK)
                return Response({'error':'Form not found'}, status=status.HTTP_200_OK)
        return Response({'error':'Not authenticated'}, status=status.HTTP_400_BAD_REQUEST)
    

    @swagger_auto_schema(operation_id="Fill Form", tags=['Forms'])
    def post(self,request,pk):
        current_user = request.user.id
        if current_user:
            user = User.objects.filter(id=current_user).first()
            if user:
                form_pk = Form.objects.filter(id=pk).first()
                if form_pk:
                    check_user_fill_form = FilledForm.objects.filter(owner_id=user.id).first()
                    if check_user_fill_form:
                        return Response({'error':'You have already filled out this form'}, status=status.HTTP_200_OK)
                    form = request.data
                    if 'values' in form.keys():
                        values = form['values']
                        result = check_fill_form_key_and_values(values)
                        if result:
                            return Response({'error':result}, status=status.HTTP_200_OK)
                        return Response({'success':add_filled_form(user,form_pk,values)}, status=status.HTTP_201_CREATED)
                    return Response({'error':'Something went wrong'}, status=status.HTTP_200_OK)
                return Response({'error':'Form not found'}, status=status.HTTP_200_OK)
        return Response({'error':'Not authenticated'}, status=status.HTTP_400_BAD_REQUEST)
    

    @swagger_auto_schema(operation_id="Delete Form", tags=['Forms'])
    def delete(self,request,pk):
        current_user = request.user.id
        if current_user:
            user = User.objects.filter(id=current_user).first()
            if user:
                form_pk = Form.objects.filter(id=pk).first()
                if form_pk:
                    if form_pk.owner_id==user or user.is_superuser:
                        form_pk.delete()
                        return Response({'success':"Form deleted"}, status=status.HTTP_200_OK)
                    return Response({'error':"You are not allowed to do this"}, status=status.HTTP_200_OK)
                return Response({'error':'Form not found'}, status=status.HTTP_200_OK)
        return Response({'error':'Not authenticated'}, status=status.HTTP_400_BAD_REQUEST)
    

class GetFilledForm(GenericAPIView):
    @swagger_auto_schema(operation_id="Get Filled Form", tags=['Filled Form'])
    def get(self,request,pk):
        current_user = request.user.id
        if current_user:
            user = User.objects.filter(id=current_user).first()
            if user:
                filled_form = FilledForm.objects.filter(owner_id=pk).first()
                data = {'id':filled_form.id,
                        'question_list_1':filled_form.question_list_1,
                        'question_list_2':filled_form.question_list_2,
                        'question_list_3':filled_form.question_list_3,
                        'question_list_4':filled_form.question_list_4,
                        'question_list_5':filled_form.question_list_5,
                        'question_list_6':filled_form.question_list_6,
                        'question_list_7':filled_form.question_list_7,
                        'question_list_8':filled_form.question_list_8,
                        'question_list_9':filled_form.question_list_9,
                        'question_list_10':filled_form.question_list_10
                }
                return Response(data, status=status.HTTP_200_OK)
        return Response({'error':'Not authenticated'}, status=status.HTTP_400_BAD_REQUEST)