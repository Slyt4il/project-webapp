from django.db import models

class Twitt(models.Model):
    # id = models.AutoField(primary_key=True)
    content = models.TextField(blank = True, null = True)
    image = models.ImageField(upload_to = 'media/post_images/', null = True, blank = True)
    likes = models.IntegerField(default = 0, null = True, blank = True)