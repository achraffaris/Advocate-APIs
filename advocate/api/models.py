from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=160)
    logo = models.ImageField(upload_to='company/')
    href = models.URLField(max_length=2048)
    summary = models.TextField(max_length=3000)

class Link(models.Model):
    youtube = models.URLField(max_length=2048)
    twitter = models.URLField(max_length=2048)
    github = models.URLField(max_length=2048)

class Advocate(models.Model):
    name = models.CharField(max_length=70)
    profile_pic = models.ImageField(upload_to='advocate/')
    short_bio = models.TextField(max_length=210)
    long_bio = models.TextField(max_length=3000)
    advocate_years_exp = models.IntegerField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    links = models.ForeignKey(Link, on_delete=models.CASCADE)

