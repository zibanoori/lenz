from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages


def logreg(request):
    return render(request, "accounts/logreg.html")


def register(request):
    if request.method == "POST":
        username = request.POST.get["username"]
        password = request.POST.get["password"]

        if User.objects.filter(username=username).exists():
            print("""
            THIS EMAIL ALREADY EXITS
            """)
