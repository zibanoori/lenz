from django.shortcuts import render
from .models import  *


def index(request):
    mymodel = MyModel.objects.first()
    socials = Social.objects.order_by('position')


    context = {
        "mymodel": mymodel,
        "socials": socials,
    }
    return render(request, "main/index.html", context)
