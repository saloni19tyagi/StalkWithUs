from django.shortcuts import render
#  import psutil
# import socket
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import logout
# Create your views here.

def home(request):
	if 'email' in request.session:
		return render(request, "index.html", {})
	return redirect('/login/?next=%s' % request.path)