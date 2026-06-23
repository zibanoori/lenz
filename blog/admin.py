from django.contrib import admin

from blog.models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'slug')
    list_display_links = ('id','title',)
    list_editable = ('slug',)



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'published_date','send_date','is_published','views','comments')
    list_display_links = ('id','title','send_date','views','comments')
    list_editable = ('is_published',)

