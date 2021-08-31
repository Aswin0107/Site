from django.db import models

# Create your models here.
class Change(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='picture')
    decr=models.TextField()


class Actor(models.Model):
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to='actorpics')
    about=models.TextField()