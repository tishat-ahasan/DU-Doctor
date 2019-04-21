from django.db import models

# Create your models here.

class Article (models.Model):
    title       = models.TextField(null=False,blank=False)
    subject       = models.TextField()
    body       = models.TextField()