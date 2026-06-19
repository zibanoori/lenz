from django.contrib import admin
from .models import MyModel

class MoDeleteAdminMixin:
    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin, MoDeleteAdminMixin):
    def has_add_permission(self, request):
        return not MyModel.objects.exists()


    list_display = ['base_title','website_title','favicon','logo','copyright']
    list_display_links = ['favicon','logo','copyright']
    list_editable = ['base_title','website_title']
