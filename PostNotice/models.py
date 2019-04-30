from django.db import models
import datetime
# Create your models here.
from django.urls import reverse
from django.utils import timezone
from sorl.thumbnail import ImageField, get_thumbnail


class post(models.Model):
    # image = models.ImageField(upload_to='post_images')
    title = models.CharField(blank=True,null = True,max_length=100)
    description = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('show_notice')

    # def save(self, *args, **kwargs):
    #     if self.image:
    #         self.image = get_thumbnail(self.image, '500x600', quality=99, format='JPEG')
    #     super(post,self).save(*args, **kwargs)