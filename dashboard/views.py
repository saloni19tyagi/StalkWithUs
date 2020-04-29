from django.shortcuts import render
import requests
#  import psutil
# import socket
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import logout
# Create your views here.
import requests

def home(request):
	if 'email' in request.session:

		codechef_url = 'https://competitive-coding-api.herokuapp.com/api/codechef/%s' % request.session['codechef']
		response = requests.get(codechef_url)
		codechef = response.json()

		codeforcesurl = "https://codeforces.com/api/user.info?handles="+request.session['codeforces']
		codeforces = requests.request("GET", codeforcesurl).json()
		li = codeforces['result']
		codeforcesrating = li[0]

		return render(request, "index.html", {'codechefRank': codechef['rank'], 'codeforcesRating': codeforcesrating['rating']})
	return redirect('/login/?next=%s' % request.path)

