from django.shortcuts import render
import psutil
import socket
from django.http import HttpResponse

import datetime
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth import logout
# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return redirect('/login/?next=%s' % request.path)
    if request.user.is_authenticated:
        return render(request, "index.html", {})
