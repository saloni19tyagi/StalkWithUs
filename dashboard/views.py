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
from chartjs.views.lines import BaseLineChartView

codeforces = [[75, 44, 92, 11, 44, 95, 35], [15, 6, 10, 23, 43, 21, 11], [10, 18, 22, 15, 23, 13, 14],
              [87, 21, 94, 3, 90, 13, 65]]
codechef = [[11, 12, 5, 27, 15, 32, 14], [41, 92, 18, 3, 73, 87, 92], [41, 92, 18, 3, 73, 87, 92],
            [41, 92, 18, 3, 73, 87, 92]]
hackerrank = [[87, 21, 94, 3, 90, 13, 65], [87, 21, 94, 3, 90, 13, 65], [87, 21, 94, 3, 90, 13, 65],
              [87, 21, 94, 3, 90, 13, 65]]

data = [200, 50, 125, 56, 89, 19]
labels = ['accepted', 'partially accepted', 'wrong', 'TLE', 'Compile Error', 'Runtime Error']

def home(request):
    if 'email' in request.session:
        codechef_url = 'https://competitive-coding-api.herokuapp.com/api/codechef/%s' % request.session['codechef']
        response = requests.get(codechef_url);
        codechef = response.json();

        codeforcesurl = "https://codeforces.com/api/user.info?handles=" + request.session['codeforces']
        codeforces = requests.request("GET", codeforcesurl).json()
        li = codeforces['result']
        codeforcesrating = li[0]

        return render(request, "index.html",
                      {'codechefRank': codechef['rank'], 'codeforcesRating': codeforcesrating['rating'], 'data': data, 'labelss':labels})
    return redirect('/login/?next=%s' % request.path)


class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["January", "February", "March", "April", "May", "June", "July"]

    def get_providers(self):
        """Return names of datasets."""
        return ["codeforces", "codechef", "hackerrank"]

    def get_data(self):
        """Return 3 datasets to plot."""

        return [codeforces[0], codechef[0], hackerrank[0]]


line_chart = TemplateView.as_view(template_name='line_chart.html')
line_chart_json = LineChartJSONView.as_view()
