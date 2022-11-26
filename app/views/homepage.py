from django.shortcuts import render
from app.models.course import Course
from app.models.model_signin import SIGNUP


# Create your views here.
def home(request):
    value = Course.objects.all()
    user = None
    if request.session.get('email'):
        email = request.session.get('email')
        user = SIGNUP.objects.get(email=email)
    context = {
        'courses': value,
        'user': user,
    }
    return render(request, 'home.html', context)
