from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username

class ImageEditting(models.Model):
    img = models.ImageField()


class Client(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=11)
    image = models.ImageField()
    doc = models.DateField()

    def __str__(self):
        return self.name
