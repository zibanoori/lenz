from django.shortcuts import render
from .models import  *


def index(request):
    mymodel = MyModel.objects.first()
    socials = Social.objects.all()


    context = {
        "mymodel": mymodel,
        "socials": socials,
    }
    return render(request, "main/index.html", context)
