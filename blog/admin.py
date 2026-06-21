from django.contrib import admin

from blog.models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'title', 'author', 'views', 'comments']
    list_display_links = ['id']
    list_editable = ['title', 'author', 'views']