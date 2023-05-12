from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from .serializers import StudentSerializer
from .models import Student



# Create your views here.

@csrf_exempt
def studentApi(request):
    if request.method == 'GET':
        data = Student.objects.all()
        student_serializer = StudentSerializer(data, many=True)
        return Response(
            {
                'Data': student_serializer.data
            }, status=status.HTTP_200_OK
        )
    elif request.method == 'POST':
        student_data = JSONParser().parse(request)
        student_serializer = StudentSerializer(student_data, many=True)
        if student_serializer.is_valid():
            student_serializer.save()
            return Response(
                {
                    'Message': 'Added Successfully'
                }, status=status.HTTP_201_CREATED
            )
        return Response(
            {
                'Message': 'Failed To Add...'
            }, status=status.HTTP_400_BAD_REQUEST
        )
    elif request.method == 'PUT':
        student_data = JSONParser().parse(request)
        student = Student.objects.get(pk=id)
        student_serializer = StudentSerializer(student, many=True)
        if student_serializer.is_valid():
            student_serializer.save()
            return Response(
                {
                    'Message': 'Updated Successfully'
                }, status=status.HTTP_200_OK
            )
        return Response(
            {
                'Message': 'Failed to Update....'
            }
        )
    elif request.method == 'DELETE':
        student = Student.objects.get(pk=id)
        student.delete()
        return Response(
            {
                'Message': 'Deleted Successfully'
            }, status=status.HTTP_200_OK
        )