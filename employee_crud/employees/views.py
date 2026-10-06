from django.shortcuts import render, get_object_or_404
from django.views import View
from rest_framework.views import APIView

from employees import serializers
from employees.models import Employee
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response

from employees.serializers import EmployeeSerializer


# Create your views here.

#APIView for reading all employee records
class EmployeeList(APIView):
    def get(self,request):
        qs=Employee.objects.all()
            #Reads all employee records from Employee table(qs)

        serializer_instance = EmployeeSerializer(qs,many=True)
            #EmployeeSerializer converts qs into python native types
            #qs contains more than one record so we use many=True

        return Response(data=serializer_instance.data)
            #sends python data as json using Response class

from json import loads

#APIVIew for creating a new employee record
class EmployeeCreate(APIView):
    #View receives data as request.data(client side data -python native type)
    #calls Serializer class for deserialization. Here we pass request.data as argument
    #After validation serializer saves data as model object inside db table


    def post(self,request):
        serializer_instance = EmployeeSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

class EmployeeDetail(APIView):
    def get(self,request,i):
        # mo=Employee.objects.get(id=i)
        mo=get_object_or_404(Employee,id=i)
        serializer_instance = EmployeeSerializer(mo)
        return Response(data=serializer_instance.data)


class EmployeeFullUpdate(APIView):
    def put(self,request,i):
        e=get_object_or_404(Employee,id=i)
        serializer_instance = EmployeeSerializer(e,request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

class EmployeePartialUpdate(APIView):
    def patch(self,request,i):
        e = get_object_or_404(Employee, id=i)
        serializer_instance = EmployeeSerializer(e,request.data,partial=True)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

class EmployeeDelete(APIView):
    def delete(self,request,i):
        e=get_object_or_404(Employee,id=i)
        # serializer_instance=EmployeeSerializer(e)
        e.delete()

        return Response({"message":"deleted"})