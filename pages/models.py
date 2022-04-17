from django.db import models

# Create your models here.

class HomepageBanner(models.Model):
    banner_title = models.CharField(max_length=200)
    banner_subtitle = models.CharField(max_length=200)
    banner_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"{self.id} | {self.banner_title}"

class Blog(models.Model):
    blog_title = models.CharField(max_length=250)
    blog_image = models.ImageField(upload_to='images/')
    blog_desc = models.TextField()

    def __str__(self):
        return f"{self.id} | {self.blog_title}"