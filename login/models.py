from django.db import models

# Create your models here.
class userdata(models.Model):

    id = models.AutoField(primary_key = True)
    first_name = models.CharField(max_length = 50, default = "")
    last_name = models.CharField(max_length = 50, default = "")
    email = models.EmailField(max_length=50, unique=True, blank=False, default="")
    password = models.CharField(max_length=50,default="")
    institute = models.TextField(default="", blank=True)
    handle = models.TextField(max_length=20, unique=True, default="")
    codechef = models.URLField(blank=True, default="")
    codeforces = models.URLField(blank=True, default="")
    hackerrank = models.URLField(blank=True, default="")
    hackerearth = models.URLField(blank=True, default="")
    spoj = models.URLField(blank=True,default="")
    linkedin = models.URLField(blank=True, default="")
    github = models.URLField(blank=True, default="")

    def __str__(self):
        return self.email
