from django.contrib import admin
from .models.course import Course, Tag, Learing, Prerequsite
from .models import Video
from .models import Payment
from .models import UserCourse


class TagAdmin(admin.TabularInline):
    model = Tag


class LearningAdmin(admin.TabularInline):
    model = Learing


class PrerequsiteAdmin(admin.TabularInline):
    model = Prerequsite


class videoAdmin(admin.TabularInline):
    model = Video


class CourseAdmin(admin.ModelAdmin):
    inlines = [TagAdmin, LearningAdmin, PrerequsiteAdmin, videoAdmin]


# Register your models here.
admin.site.register(Course, CourseAdmin)
admin.site.register(Video)
admin.site.register(UserCourse)
admin.site.register(Payment)
