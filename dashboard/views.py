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
		response = requests.get(codechef_url);
		codechef = response.json();
		url = "https://codeforces.com/api/user.info?handles="+request.session['handle']
		payload = {}
		headers = {
			'Cookie': 'JSESSIONID=02249090B1061D683A8B443894284151-n1; 39ce7=CFkwUcjt'
		}
		response = requests.request("GET", url, headers=headers, data = payload)

		# print(response.json())
		response = response.json()
		# print(response['result'])
		li = response['result']
		data = li[0]
		# print(data['rating'])

		return render(request, "index.html", {'codechefRank' : codechef['rank'],'codeforcesRating' : data['rating']})
	return redirect('/login/?next=%s' % request.path)

