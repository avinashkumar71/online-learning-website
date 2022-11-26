from django.shortcuts import render
from app.models.user_course import UserCourse
from app.models.course import Course


def mycourse(request):
    x = []
    if request.session:
        email = request.session.get('email')
        user_course = UserCourse.objects.filter(user=email)
        for uc in user_course:
            course = Course.objects.get(name=uc.course)
            x.append(course)

    context = {
        'user_course': x,
    }
    return render(request, 'mycourse.html', context)
