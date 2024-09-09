from django.db import models

# Create your models here.
class Receipe(models.Model):
    receipe_name = models.CharField(max_length=100)
    receipe_description = models.TextField(max_length=1000)
    receipe_instructions = models.TextField(default=None) 
    receipe_image = models.ImageField(upload_to='receipes') 
