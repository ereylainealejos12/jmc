from django.shortcuts import render
from .models import Teacher,Student
# Create your views here.
def home(request):
    return render(request, 'jmc/home.html')

def student(request):
    obj = Student.objects.all()
    return render(request, 'jmc/student.html', {
        'obj': obj
    })

def teacher(request):
    obj = Teacher.objects.all()
    return render(request, 'jmc/teacher.html', {
        'obj': obj
    })