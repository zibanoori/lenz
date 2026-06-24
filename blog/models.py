from django.db import models
from datetime import datetime
from author.models import Author
from django.utils.text import slugify

class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"

    title = models.CharField(max_length=50, blank=True)
    slug = models.CharField(max_length=50, blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Post(models.Model):
    class Meta:
        verbose_name_plural = "Posts"

    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    author = models.ForeignKey(Author,on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200,blank=True)
    slug = models.SlugField(max_length=250,blank=True, unique=True)
    image = models.ImageField(upload_to='blog/%Y/%m',blank=True)
    send_date = models.DateTimeField(default=datetime.now, blank=True)
    views = models.PositiveIntegerField(default=0,blank=True)
    comments = models.PositiveIntegerField(default=0,blank=True)
    full_text = models.TextField(blank=True)
    abstract = models.TextField(blank=True)
    tags = models.CharField(max_length=200,blank=True)
    is_published = models.BooleanField(default=False)
    published_date = models.DateField(default=datetime.now, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            new_slug = base_slug
            counter = 1
            while Post.objects.filter(slug=new_slug).exists():
                new_slug = f"{base_slug}_{counter}"
                counter += 1
            self.slug = new_slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title + '('+ str(self.views) + ' views)'