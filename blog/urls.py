from django.urls import path
from .views import *

urlpatterns = [path("post/<slug:post_slug>/",post_delete, name="post_detail")]
