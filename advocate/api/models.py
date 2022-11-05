from django.db import models

class Advocate(models.Model):
    profile_pic = models.ImageField(upload_to='advocate/')
    username = models.CharField(max_length=70)
    name = models.CharField(max_length=70)
    bio = models.TextField(max_length=3000)
    twitter = models.URLField(max_length=2048)
    def __str__(self):
        return self.name
