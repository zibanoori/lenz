from django.shortcuts import render
from .models import  MyModel


def index(request):
    mymodel = MyModel.objects.first()
    return render(request, "main/index.html")
