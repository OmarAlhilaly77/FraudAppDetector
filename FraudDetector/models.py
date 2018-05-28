from django.db import models

# Create your models here.
class post(models.Model):
    url = models.CharField(max_length=2083)
