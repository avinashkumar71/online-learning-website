from django.db import models


class SIGNUP(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class SIGNIN(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=10)
