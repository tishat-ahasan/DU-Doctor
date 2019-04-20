from django.db import models
from django.urls import reverse

# Create your models here.
class Product (models.Model):
    title            = models.TextField(null = False,blank = False);
    description      = models.TextField(null = False,blank = False);
    price            = models.DecimalField(max_digits=25,decimal_places=4);
    summary          = models.TextField(default="This is cool!");

    def get_absolute_url(self):
        return reverse("product:product_details",kwargs={"my_id":self.id})