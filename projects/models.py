from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    phtype = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")

# Create your models here.
