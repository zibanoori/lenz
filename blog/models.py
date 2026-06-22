from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"



    slug = models.CharField(max_length=50,blank=True)
    title = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title
