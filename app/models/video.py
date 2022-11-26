from django.db import models
from .course import Course


class Video(models.Model):
    title = models.CharField(max_length=30, null=False)
    course = models.ForeignKey(Course, max_length=20, null=False, on_delete=models.CASCADE)
    serial_number = models.IntegerField(null=False)
    video_id = models.CharField(max_length=60, null=False)
    is_preview = models.BooleanField(null=False)

    def __str__(self):
        return self.title
