from email.policy import default
from django.db import models

# Create your models here.

class Homepage_banner(models.Model):
    Banner_title = models.CharField(max_length=200)
    Banner_subtitle = models.CharField(max_length=200)
    Banner_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.Banner_title