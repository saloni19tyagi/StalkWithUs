from django.shortcuts import render
import requests
#  import psutil
# import socket
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import logout
# Create your views here.
import requests
from django.views.generic import TemplateView
from dashboard.leaderboard import createLeaderBoard


from dashboard import models
from login import models
from login.models import userdata

codeforces = [[75, 44, 92, 11, 44, 95, 35], [15, 6, 10, 23, 43, 21, 11], [10, 18, 22, 15, 23, 13, 14],
              [87, 21, 94, 3, 90, 13, 65]]
codechef = [[11, 12, 5, 27, 15, 32, 14], [41, 92, 18, 3, 73, 87, 92], [41, 92, 18, 3, 73, 87, 92],
            [41, 92, 18, 3, 73, 87, 92]]
hackerrank = [[87, 21, 94, 3, 90, 13, 65], [87, 21, 94, 3, 90, 13, 65], [87, 21, 94, 3, 90, 13, 65],
              [87, 21, 94, 3, 90, 13, 65]]


def home(request):
    if 'email' in request.session:
        return render(request, "index.html")
    return redirect('/login/?next=%s' % request.path)


def viewProfile(request):
    if 'email' in request.session:
        user = userdata.objects.get(email=request.session['email'])
        return render(request, "profile.html",{'user': user})
    return redirect('/login/?next=%s' % request.path)


def friends(request):
    return render(request, "friends.html")


def todolist(request):
    return render(request, "toDoList.html")


def aboutus(request):
    return render(request, "aboutus.html")


def recentsubmissions(request):
    return render(request, "recent_friends_submissions.html")

def trendingProblems(request):
    return render(request, "trending_problems.html")



def leaderboard(request):
    createLeaderBoard()
    return render(request, "leaderboard.html")
