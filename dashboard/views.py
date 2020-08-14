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
# from chartjs.views.lines import BaseLineChartView

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


def leaderboard(request):
    return render(request, "leaderboard.html")


def aboutus(request):
    return render(request, "aboutus.html")


def recentsubmissions(request):
    return render(request, "recent_friends_submissions.html")

def trendingProblems(request):
    return render(request, "trending_problems.html")



# def refreshData(request):
#     codechef_url = 'https://competitive-coding-api.herokuapp.com/api/codechef/%s' % request.session['codechef']
#     response = requests.get(codechef_url)
#     codechef = response.json();
#     codeforcesurl = "https://codeforces.com/api/user.info?handles=" + request.session['codeforces']
#     codeforces = requests.request("GET", codeforcesurl).json()
#     li = codeforces['result']
#     codeforcesrating = li[0]

#     user = models.userdata.objects.get(email = request.session['email'])
#     user.codeforcesRating = codeforcesrating['rating']
#     user.codechefRating = codechef['rank']
#     user.save()
#     print(codeforcesrating['maxRating'])
#     print(codechef['rank'])

#     return render(request, "profile.html")


# class LineChartJSONView(BaseLineChartView):
#     def get_labels(self):
#         """Return 7 labels for the x-axis."""
#         return ["January", "February", "March", "April", "May", "June", "July"]

#     def get_providers(self):
#         """Return names of datasets."""
#         return ["codeforces", "codechef", "hackerrank"]

#     def get_data(self):
#         """Return 3 datasets to plot."""

#         return [codeforces[0], codechef[0], hackerrank[0]]


# line_chart = TemplateView.as_view(template_name='line_chart.html')
# line_chart_json = LineChartJSONView.as_view()
