from django.contrib import admin

from blog.models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_display_links = ('title',)
    list_editable = ('slug',)
