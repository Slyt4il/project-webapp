from django.db import models

from django.contrib.auth.models import User


class Twitt(models.Model):
    # id = models.AutoField(primary_key=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    content = models.TextField(blank = True, null = True)
    image = models.ImageField(upload_to = 'media/post_images/', null = True, blank = True)
    likes = models.IntegerField(default = 0, null = True, blank = True)
    timestamp = models.DateTimeField(auto_now_add = True, null = True, blank = True)

    #class Meta:
        #ordering = ['-id']

    def serialize(self):
        return {
            "id" : self.id,
            "content" : self.content,
            "likes" : self.likes,
            "timestamp" : self.timestamp
        }
    
    def __str__(self):
        return f"[{self.id}] {self.content}"[0:74]