from django.db import models

# Create your models here.
class leaderboard(models.Model):

    id = models.AutoField(primary_key = True)
    username = models.CharField(max_length= 50, default= "", unique=True)
    rating = models.TextField(default=0, blank=True)

    
def __str__(self):

    return ' '.join([

        self.username,
        self.rating

    ])


