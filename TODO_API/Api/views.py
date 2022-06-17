from urllib import response
from django.shortcuts import render
from Api.serializers import TodoSerializer
from Api.models import Todo
from rest_framework.response import Response

from Api.serializers import RegisterSerializer
from Api.models import Register
from rest_framework.views import APIView
# from rest_framework.filters import SearchFilter
# from django_filters.rest_framework import DjangoFilterBackend



# Create your views here.


# class Registrations(APIView):
#     def get(self, request):                                    
#         registration = Register.objects.all()
#         registration_serializer = RegisterSerializer(
#             instance=registration, many=True, context={'request': request})
#         return Response(registration_serializer.data)


class UserRegister(APIView):
    def get(self, request):
        registration = Register.objects.all()
        registration_serializer = RegisterSerializer(
            instance=registration, many=True, context={'request': request})
        return Response(registration_serializer.data)

    def post(self, request):
        try:
            registration_serializer = RegisterSerializer(
                data=request.data)
            if registration_serializer.is_valid():
                registration_serializer.save()
                return Response(registration_serializer.data)
            return Response(registration_serializer.errors)

        except Exception as ex:
            print("ex", ex)
            return Response("Exception")

class login(APIView):
    def post(self,request):
        email = request.data['email']
        password = request.data['password']
        try:
            if Register.objects.filter(email=email, password=password).exists():
                user = Register.objects.get(email=email, password=password)
                

                if user.email == email and user.password == password:
                    return Response(
                        "Login Successful"
                    )

                else:
                    return Response({
                        "error": "Invalid data"
                    })

            else:
                return Response({
                    "error": "Invalid data"
                })

        except Exception as ex:
            return Response({
                'error': str(ex)
            })


class NewRecord(APIView):
    

    def get (self,request):
        
        record = Todo.objects.all()
        record_serializer = TodoSerializer(record, many=True,)
            #  context={'request': request})
        return Response(record_serializer.data)

    def post(self, request):                           
        role_serializer = TodoSerializer(data=request.data)
        if role_serializer.is_valid(raise_exception=False):
            role_serializer.save()
            return Response(role_serializer.data)
        return Response(role_serializer.errors)

    
    def put(self, request, id):

        todo_obj = Todo.objects.get(id=id)
        todo_serializer = TodoSerializer(
            Todo, data=request.data)
            
        if todo_serializer.is_valid():
            todo_serializer.update(
                todo_obj, todo_serializer.validated_data)
        
            return Response(
                "Record Updated "
            )
        else:
            return Response({
                "error": todo_serializer.errors
            })

    def delete(self, request,id):
        task = Todo.objects.get(id=id)
        task.delete()
        return Response("Record deleted")



# class SearchRecord(APIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer
#     filter_backends = (DjangoFilterBackend, SearchFilter)
#     search_fields = ['title']


#     def get(self,request):
#         record = (Todo.objects.all())

#         record_serializer = TodoSerializer(record, many=True,)
#         #  context={'request': request})
#         return Response(record_serializer.data)

