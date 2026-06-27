from django.contrib import admin
from blog.models import *
from django.utils.html import format_html
from django.urls import reverse


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'slug')
    list_display_links = ('id','title',)
    list_editable = ('slug',)



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'published_date','send_date','is_published','views','comments','view_post_link',)
    list_display_links = ('id','title','send_date','views','comments','published_date','view_post_link')
    list_editable = ('is_published',)

    def view_post_link(self,obj):
        if obj.slug:
            url = reverse('post_detail',args=[obj.slug])
            return format_html('<a style = "background-color:green; color:#fff; padding: 5px 10px; border-radius:5px; text-decoration:none"href="{}" target="blank">👁️View Post</a>',url)
        return "No Slugs"
    view_post_link.short_description = 'Direct link'