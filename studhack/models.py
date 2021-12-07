from django.db import models

descr = """ Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
                            Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
                            when an unknown printer took a galley of type and scrambled it to make a type specimen book. """
#Table: tasks

class Tasks(models.Model):
    #id = models.IntegerField(primary_key=True, unique=True)
    task_name = models.CharField(max_length=255)
    expert = models.CharField(max_length=255)
    brief_descr = models.CharField(max_length=50, default=descr)
    #stack = models.TextField()
    photo = models.ImageField(upload_to="photos/", verbose_name="Фото", null=True)
    #participants = One to Many
    def __str__(self):
        return self.task_name

    # def get_absolute_url(self):
    #     return reverse('post', kwargs={'post_id': self.pk})        

class Teams(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    team_name = models.CharField(max_length=255)
    task = models.ForeignKey('Tasks', on_delete=models.PROTECT, null=True)
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