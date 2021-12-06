from django.db import models


#Table: tasks

class Tasks(models.Model):
    #id = models.IntegerField(primary_key=True, unique=True)
    task_name = models.CharField(max_length=255)
    expert = models.CharField(max_length=255)
    #description = models.TextField()
    #stack = models.TextField()
    #photo = models.ImageField(upload_to=f"photos/{id}")
    #participants = One to Many
    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('post', kwargs={'post_id': self.pk})        

class Teams(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    team_name = models.CharField(max_length=255)
    #task
    #team_photo = models.ImageField(upload_to=f"photos/{id}")
    
    # team_captain - One to One ?
    def __str__(self):
        return self.team_name

class Participants(models.Model):
    full_name = models.CharField(max_length=255)
    #password?
    team = models.ForeignKey('Teams', on_delete=models.PROTECT, null=True) #one to Many?

    def __str__(self):
        return self.full_name