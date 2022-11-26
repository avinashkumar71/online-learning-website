from django.shortcuts import render
from django.http import HttpResponse
from app.models.course import Course
from app.models.video import Video
from app.models.payment import Payment
from app.models.user_course import UserCourse


def courseview(request, slug):
    course = Course.objects.get(slug=slug)
    serial_number = request.GET.get('lecture')
    if serial_number is None:
        serial_number = 1
    try:
        video = Video.objects.get(serial_number=serial_number, course=course)
    except:
        return HttpResponse('<h1>Video not publish Yet</h1>')

    email = request.session.get('email')
    user_course = UserCourse.objects.filter(user=email, course=course.name)
    payments = Payment.objects.filter(user=email, course=course)
    if len(payments) == 0:
        if video.is_preview is False:
            return HttpResponse('<h1>To continue please purchased this course</h1>')
        else:
            return render(request, 'courseview.html', {'course': course, 'videos': video})
    elif user_course:
        return render(request, 'courseview.html', {'course': course, 'videos': video})
    else:
        if video.is_preview is False:
            return HttpResponse('<h1>To continue please purchased this course</h1>')
        else:
            return render(request, 'courseview.html', {'course': course, 'videos': video})
