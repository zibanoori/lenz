from django.contrib import admin, messages
from .models import *
from django.utils.html import format_html
from django.urls import reverse, path
from django.shortcuts import get_object_or_404, redirect


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug']
    list_display_links = ['id']
    list_editable = ['title', 'slug']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'send_date', 'published_date', 'views', 'comments',
                    'view_post_link', 'status_toggle']
    list_display_links = ['title', 'send_date', 'published_date']

    def view_post_link(self, obj):
        if obj.slug:
            url = reverse('post_detail', args=[obj.slug])
            return format_html('<a style="background-color: #417690; color: #fff; padding: 5px 10px; border-radius: 4px; text-decoration: none" href="{}" target="_blank">👁️ View Post </a>', url)
        return "No Slug"

    view_post_link.short_description = "Direct link"

    def status_toggle(self, obj):
        if obj.is_published:
            color = "green"
            text = "Published ✅"
            action_text = "Unpublish"
        else:
            color = "red"
            text = "Unpublished ❌"
            action_text = "Publish"

        url = reverse("admin:blog_post_toggle_publish", args=[obj.pk])

        return format_html(
            '<a href="{}" style="color: {}; font-weight: bold; text-decoration: none">'
            '{} ({})'
            '</a>',
            url, color, text, action_text
        )
        
    status_toggle.short_description = "Status"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                '<int:post_id>/toggle-publish',
                self.admin_site.admin_view(self.toggle_publish_view),
                name="blog_post_toggle_publish"
            ),
        ]
        return custom_urls + urls
    
    def toggle_publish_view(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        post.is_published = not post.is_published
        post.save()

        state = "published" if post.is_published else "unpublished"
        self.message_user(
            request, f'Post "{post.title}" has been {state}.',
            messages.SUCCESS
        )

        return redirect(request.META.get('HTTP_REFERER', reverse('admin:blog_post_changelist')))
