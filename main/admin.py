from django.contrib import admin
from .models import MyModel


@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ['base_title','website_title','favicon','light_logo','dark_logo','copyright']
    list_display_links = ['favicon','dark_logo','light_logo','copyright']
    list_editable = ['base_title','website_title']
