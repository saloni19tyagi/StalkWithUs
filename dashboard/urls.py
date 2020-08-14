"""StalkWithUs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

import dashboard
from dashboard import views
# from .views import line_chart, line_chart_json

urlpatterns = [
    path('dashboard/', views.home, name='home'),
    path('profile/', views.viewProfile, name='profile'),
    path('friends/', views.friends, name='friends'),
    path('todolist/', views.todolist, name='todolist'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('recentsubmissions/', views.recentsubmissions, name='recentsubmissions'),
    path('aboutus/', views.aboutus, name='aboutus'),
    # path('chart/', line_chart, name='line_chart'),
    # path('chartJSON/', line_chart_json, name='line_chart_json'),
    # path('refreshData', views.refreshData, name='refreshData')
]
