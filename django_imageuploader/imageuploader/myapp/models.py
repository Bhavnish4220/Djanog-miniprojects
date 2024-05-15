from django.db import models

class image(models.Model):
    photo=models.ImageField(upload_to="myimage")
    date=models.DateTimeField(auto_now_add=True)