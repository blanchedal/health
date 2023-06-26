from django.db import models

# Create your models here.

class Bmi(models.Model):
    name = models.CharField(max_length=100)
    height = models.FloatField()
    weight = models.FloatField()
    user_bmi=models.DecimalField(null=True,blank=True,max_digits=5,decimal_places=2)
    level = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name