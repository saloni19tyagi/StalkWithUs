from django.db import models

class userdata(models.Model):
	username: models.CharField(max_length=20)
	password: models.CharField(max_length=20)
	email:models.CharField(max_length=20)