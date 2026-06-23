from .models import *


def site_settings(request):
    mymodel = MyModel.objects.first()
    socials = Social.objects.order_by('position')

    context = {
        "mymodel": mymodel,
        "socials": socials,
    }