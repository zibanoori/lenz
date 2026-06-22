from django.contrib import admin

from author.models import Author


@admin.register(Author)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','first_name', 'last_name','email')
    list_display_links = ('id','first_name', 'last_name','email')


