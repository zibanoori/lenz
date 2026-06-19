from django.shortcuts import render
from .models import  MyModel


def index(request):
    mymodel = MyModel.objects.first()

    context = {
        "mymodel": mymodel,
    }
    return render(request, "main/index.html", context)
