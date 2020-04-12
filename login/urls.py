from django.conf.urls import url
from login import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    # url(r'^$', views.HomePageView.as_view(), name='home'), # Notice the URL has been named
    # url(r'^about/$', views.AboutPageView.as_view(), name='about'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(),name='login'),
    url(r'^logout/$',  auth_views.LogoutView.as_view(), name='logout')
]