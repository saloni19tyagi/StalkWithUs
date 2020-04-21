from django.shortcuts import render
# import psutil
# import socket
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import logout
# Create your views here.
from codeforces import api
import requests

def home(request):
    return render(request, 'index.html')

def viewProfile(request):
    url = "https://codeforces.com/api/user.info?handles=vandita_1081"
    response = requests.request("GET", url)
    print(response.text.encode('utf8'))
    response = response.json()
    return render(request, 'profile.html', {'submissionData': response})
