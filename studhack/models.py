from django.db import models


#Table: tasks

class Tasks(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    task_name = models.CharField(max_length=255)
    expert = models.CharField(max_length=255)
    #description = models.TextField()
    #stack = models.TextField()
    #photo = models.ImageField(upload_to=f"photos/{id}")
    #participants = One to Many        

class Teams(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    team_name = models.CharField(max_length=255)
    #task
    #team_photo = models.ImageField(upload_to=f"photos/{id}")
    # team_members - One to Many
    # team_captain - One to One ?

class Participants(models.Model):
    full_name = models.CharField(max_length=255)
    #password?
    team = models.CharField(max_length=255, default=None, null=True) #one to Many?


    