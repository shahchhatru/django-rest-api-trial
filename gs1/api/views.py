from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

from .models import Student
from .serializers import StudentSerializer

#Model Object - Single Student Data

def student_detail(request,pk):
    stu=Student.objects.get(id=pk)
    serializer=StudentSerializer(stu)
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')

#all student data
def student_list(request):
    stu_all=Student.objects.all()
    serializer=StudentSerializer(stu_all,many=True)
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type="application/json")



