from django.db import models
from .user_course import UserCourse


class Payment(models.Model):
    order_id = models.CharField(max_length=50, null=False)
    payment_id = models.CharField(max_length=50)
    user_course = models.ForeignKey(UserCourse, blank=True, null=True, on_delete=models.CASCADE)
    user = models.EmailField()
    course = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
