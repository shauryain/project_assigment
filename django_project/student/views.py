from django.shortcuts import render
from .models import Student

# Create your views here.


def index(request):
    return render(request,"student/index.html",{
        "student":Student.objects.all()
    })