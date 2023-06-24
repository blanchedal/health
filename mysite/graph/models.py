from django.db import models

class fruits(models.Model):
    name = models.CharField(max_length=50)
    value = models.IntegerField()

# Create your models here.
