from django.shortcuts import render
from rest_framework import generics,status
from employees.models import Employee
from rest_framework.response import Response

from employees.serializers import EmployeeSerializer

# Create your views here.
class EmployeeListCreateView(generics.ListCreateAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
       queryset = Employee.objects.all()

       department = self.request.query_params.get('department')
       role = self.request.query_params.get('role')

       if department:
              queryset = queryset.filter(department=department)

       if role:
             queryset = queryset.filter(role=role)
            
       return queryset
    
    def create(self, request,*args,**kwargs):
         is_many = isinstance(request.data,list)

         serializer = self.get_serializer(
              data = request.data,
              many = is_many
              
         )
         serializer.is_valid(raise_exception=True)
         serializer.save()

         return Response(
              serializer.data,
              status=status.HTTP_201_CREATED
         )


    
class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
     queryset=Employee.objects.all()
     serializer_class = EmployeeSerializer