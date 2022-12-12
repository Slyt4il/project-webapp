from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    name = models.CharField(default = 'New User', max_length=200, null=True)
    title = models.CharField(default = 'Newbie', max_length=200, null=True)
    desc_text = 'When something is important enough, you do it even if the odds are not in your favor.'
    desc = models.CharField(default = desc_text, max_length=200, null=True)
    profile_img =  models.ImageField(default = 'media/profile_images/default.jpg', upload_to = 'media/profile_images/', null = True, blank = True)

    def __str__(self):
        return f"{self.user.username}'s profile"