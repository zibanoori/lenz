from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"


    image = models.ImageField(upload_to="blog/category/", blank=True)
    slug = models.CharField(max_length=50,blank=True)
    title = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    author = models.CharField(max_length=50, blank=True)
    date = models.CharField(max_length=100, blank=True)
    views = models.PositiveIntegerField(default=0)
    comments = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title
