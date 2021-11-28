from django.db import models

# Create your models here.


class UserReg(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    password = models.CharField(max_length=16)


class Images(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=32)

