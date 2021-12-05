from django.db import models


#Table: tasks

class Tasks(models.Model):
    id = 0
    task_name = models.CharField(max_length=255)
    #sphere
    expert = models.CharField(max_length=255)
    description = models.TextField()
    stack = models.TextField()
    photo = models.ImageField(upload_to=f"photos/{id}")        

    