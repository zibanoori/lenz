from django.db import models

class MyModel(models.Model):
    class Meta:
        verbose_name ="Main Details"
        verbose_name_plural = "Main Details"

    base_title = models.CharField(max_length=50, blank=True)
    website_title = models.CharField(max_length=50, blank=True)
    favicon = models.ImageField(upload_to="main", blank=True)
    light_logo = models.ImageField(upload_to="main", blank=True)
    dark_logo = models.ImageField(upload_to="main", blank=True)
