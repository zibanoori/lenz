from django.db import models


class MyModel(models.Model):
    class Meta:
        verbose_name = "Main Details"
        verbose_name_plural = "Main Details"

    base_title = models.CharField(max_length=50, blank=True)
    website_title = models.CharField(max_length=50, blank=True)
    favicon = models.ImageField(upload_to="main", blank=True)
    logo = models.ImageField(upload_to="main", blank=True)
    copyright = models.TextField(blank=True)

    def __str__(self):
        return self.website_title


class Social(models.Model):
    class Meta:
        verbose_name = "Social"
        verbose_name_plural = "Socials"

    media = models.CharField(max_length=30, blank=True)
    icon =models.CharField(max_length=30, blank=True)
    link = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.media

