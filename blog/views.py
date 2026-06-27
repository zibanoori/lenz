from django.shortcuts import render, get_object_or_404

from .models import *


def post_detail(request, post_slug):
    post = get_object_or_404(Post,slug=post_slug)
    context = {
        "post":post
    }

    return render(request, "blog/post_details.html", context=context)
