from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.contrib import messages
from .models import officialwebsites
from .models import location
from .models import drive

from django.core.mail import send_mail
import requests
import json

# Create your views here.
def index(request):
    companydrive=drive.objects.all()
    return render(request,'index.html',{'companydrive':companydrive})

def getcompanies(request):
    comp=officialwebsites.objects.all()
    return render(request,'companies.html',{'comp':comp})

def home(request):
    return render(request,'index.html')
def learn(request):
    return render(request,'learn.html')

def videos(request):
    return render(request,'videos.html')

def button1v(request):
    return render(request,'button1v.html')
def button2v(request):
    return render(request,'button2v.html')
def button3v(request):
    return render(request,'button3v.html')

def adminlogin(request):
    return render(request,'login.html')

def contact(request):
    return render(request,'contact.html')

def search(request):
    return render(request,'search.html')

def exampreparation(request):
    return render(request,'exampreparation.html')

def about(request):
        return render(request,'about.html')

def locations(request):
    company=location.objects.all()
    return render(request,'location.html',{'company':company})
    
@csrf_exempt
def sms(request):
    URL='https://www.sms4india.com/api/v1/sendCampaign'
        # get request
    def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
        req_params = {
        'apikey':apiKey,
        'secret':secretKey,
        'usetype':useType,
        'phone': phoneNo,
        'message':textMessage,
        'senderid':senderId
         }
        return requests.post(reqUrl, req_params)
    m =request.POST['message']
    # get response
    response = sendPostRequest(URL, 'ERGUSLWCYUYBF0ZIGBOJ893U5DJLT9SV', 'K4QVVH48QUBFW7YH', 'stage', '6281430586', 'SMSIND',m)

    # print response if you want
    print(response.text)
    message_sent="message sent"
    return render(request,'contact.html',{'messagesent':message_sent})
@csrf_exempt
def mail(request):
    if request.method=="POST":
        message_name=request.POST['name']
        message_email=request.POST['email']
        message_subject=request.POST['subject']
        message=request.POST['message']
        send_mail(
             message_subject,    #subject
             message,            #message
             message_email,      #from email
             ['sathyasree0809@gmail.com'],#to mail

         )
        email="email received."
        return render(request,'contact.html',{'message_name':message_name,'email':email})
    else:
        return render(request,'contact.html')




