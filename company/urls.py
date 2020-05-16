from django.urls import path
from django.conf.urls import url
from . import views
app_name='company'

urlpatterns=[

    path('',views.index,name='index'),
    path('home',views.home,name='home'),
    path('getcompanies',views.getcompanies,name='getcompanies'),
    path('videos',views.videos,name='videos'),
    path('button1v',views.button1v,name='button1v'),
    path('button2v',views.button2v,name='button2v'),
    path('button3v',views.button3v,name='button3v'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('contact',views.contact,name='contact'),
    path('exampreparation',views.exampreparation,name='exampreparation'),
    path('about',views.about,name='about'),
    path('locations',views.locations,name='locations'),
    path('learn',views.learn,name='learn'),
    path('sms',views.sms,name='sms'),
    path('mail',views.mail,name='mail'),
]