from django.db import models


class UserCourse(models.Model):
    user = models.EmailField(max_length=20)
    course = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
