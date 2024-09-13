from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Receipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    receipe_name = models.CharField(max_length=100)
    receipe_description = models.TextField(max_length=1000, null=True, blank=True)
    receipe_ingredients = models.TextField(null=True, blank=True)
    receipe_category = models.CharField(max_length=100, null=True, blank=True)
    receipe_instructions = models.TextField(null=True, blank=True)
    cooking_time = models.IntegerField(null=True, blank=True)
    receipe_author = models.CharField(max_length=100, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    difficulty = models.CharField(max_length=100, null=True, blank=True)
    receipe_image = models.ImageField(upload_to='receipes', null=True, blank=True)

    def __str__(self):
        return self.receipe_name
