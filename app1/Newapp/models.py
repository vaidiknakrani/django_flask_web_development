from django.db import models

class Person(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=50)
    pH = models.IntegerField(null=True)