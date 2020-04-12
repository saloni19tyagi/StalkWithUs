from django.shortcuts import render
# import psutil
# import socket
from django.http import HttpResponse

import datetime
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth import logout
# Create your views here.

def home(request):
    return render(request, "index.html", {})
