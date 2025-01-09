from django.db import models

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    # image = models.CharField(default=None, blank=True, null=True, max_length=2000)
    image = models.ImageField(upload_to='main_app/static/uploads/', default="")