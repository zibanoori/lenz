
from django.urls import path
from .views import *

urlpatterns = [
    path("login-register", logreg, name="logreg"),
    path("signup",register, name="signup"),
    path("signin", logreg, name="signin"),

    path("signout", logreg, name="signout"),
]