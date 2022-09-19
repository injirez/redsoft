from django.db import models


class Photo(models.Model):
    file = models.ImageField(upload_to='media/')


class Client(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    birth_date = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=8, choices=[('мужской', 'мужской'), ('женский', 'женский')])
    photo = models.OneToOneField(Photo, on_delete=models.CASCADE)

