from django.urls import path
from .views import *

urlpatterns = [
    path("login-register", logreg, name="post_detail")

]
