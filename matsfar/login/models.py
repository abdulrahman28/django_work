from django.db import models

# Create your models here.


class detail(models.Model):
    uname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    pword = models.CharField(max_length=100)
    dept = models.CharField(max_length=100)


