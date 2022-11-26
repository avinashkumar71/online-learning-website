from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=20, null=False)
    slug = models.CharField(max_length=30, null=True, unique=True)
    description = models.CharField(max_length=30, null=True)
    price = models.IntegerField(null=False)
    discount = models.IntegerField(null=False, default=0)
    active = models.BooleanField(default=False)
    thumbnail = models.ImageField(upload_to='Thumbnail/')
    date = models.DateTimeField(auto_now_add=True)
    resource = models.FileField(upload_to='files/resourse/')
    length = models.IntegerField(null=False)

    def __str__(self):
        return self.name

class TagLearningPre(models.Model):
    description = models.CharField(max_length=20)
    course = models.ForeignKey(Course, null=False, on_delete=models.CASCADE)
    class Meta:
        abstract = True

class Tag(TagLearningPre):
    pass

class Learing(TagLearningPre):
    pass

class Prerequsite(TagLearningPre):
    pass