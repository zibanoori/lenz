from django.contrib import admin

from blog.models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'slug')
    list_display_links = ('id','title',)
    list_editable = ('slug',)



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'date','views','comments')
    list_display_links = ('id','title','date','views','comments')

