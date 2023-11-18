from django.db import models

class Person(models.Model):
    userinputvalue = models.CharField(max_length=30)
    usercalvalue = models.CharField(max_length=30)
