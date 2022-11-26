from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.models.course import Course
from app.models.user_course import UserCourse
from app.models.payment import Payment
from app.models.video import Video
from app.models.model_signin import SIGNIN, SIGNUP
import razorpay
from project.settings import *
from time import time
from django.views.decorators.csrf import csrf_exempt

client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))  # here is your razorpay key_id , key_secret


def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        email_data = SIGNUP.objects.filter(email=email)
        if len(email_data) == 0:
            data = SIGNUP(name=name, email=email, password=password)
            data.save()
            return redirect('signin')
        else:
            return redirect('signup')
    return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        email_data = SIGNUP.objects.filter(email=email, password=password)
        if len(email_data) == 1:
            request.session['email'] = email
            data = SIGNIN()
            return redirect('home')
    return render(request, 'signin.html')


def logout(request):
    request.session.clear()
    print(request.session.get('email'))
    return redirect('home')


def enroll(request, slug):  # for enroll button
    course = Course.objects.filter(slug=slug)
    course_name=course[0].name
    email = request.session.get('email')
    pymt=Payment.objects.filter(course=course_name, user=email)
    print(pymt)
    if len(pymt)==0:
        return render(request, 'order.html', {'courses': course})
    if pymt[0].status is False:
        return render(request, 'order.html', {'courses': course})
    return redirect('mycourse')

def order(request, slug):
    course = Course.objects.filter(slug=slug)
    email = request.session.get('email')
    if email is None:
        return redirect('signin')
    user = SIGNUP.objects.get(email=email)
    action = request.GET.get('action')
    order = None
    payment = None
    error = None
    try:
        user_course = UserCourse.objects.get(user=user.email, course=course[0].name)
        print(user_course)
        error = 'you are already purchased this course'
    except:
        pass
    if error is None:
        if action == 'course_payment':
            amount = ((course[0].price - (course[0].price * course[0].discount * 0.01)) * 100)
            currency = 'INR'
            notes = {
                'email': user.email,
                'name': f'{user.name}',
            }
            receipt = f'{course[0].name} {int(time())}'
            order = client.order.create({  # creating order
                'amount': amount,
                'currency': currency,
                'notes': notes,
                'receipt': receipt,
            })
            payment = Payment()
            payment.order_id = order.get('id')
            payment.user = request.session.get('email')
            payment.course = course[0].name
            payment.save()

    return render(request, 'order.html', {'courses': course, 'order': order, 'error': error})


@csrf_exempt  # this will ignore the csrf_token which required for post method
def verifypayment(request):
    if request.method == 'POST':
        data = request.POST
        try:
            client.utility.verify_payment_signature(data)  # verify signature

            razorpay_payment_id = data['razorpay_payment_id']
            razorpay_order_id = data['razorpay_order_id']

            payment = Payment.objects.get(order_id=razorpay_order_id)
            payment.payment_id = razorpay_payment_id
            payment.status = True

            usercourse = UserCourse(user=payment.user, course=payment.course)
            usercourse.save()

            payment.user_course = usercourse
            payment.save()

            return redirect('mycourse')
        except:
            return HttpResponse('<h1>Sorry ! your payment Failed</h1>')
