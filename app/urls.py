from django.urls import path
from app.views.homepage import home
from app.views.courseview import courseview
from app.views.mycourse import mycourse
from app.views.register import signup, signin, logout, order, verifypayment, enroll

urlpatterns = [
    path('', home, name='home'),
    path('course/<str:slug>', courseview, name='courseview'),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('logout/', logout, name='logout'),
    path('check_out/<str:slug>', order, name='order'),
    path('payment/', verifypayment, name='verifypayment'),
    path('mycourse/', mycourse, name='mycourse'),
    path('enroll/<str:slug>', enroll, name='enroll'),
]
