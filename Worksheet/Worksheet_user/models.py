from django.db import models
from django.contrib.auth.models import User
from datetime import datetime 




# Create your models here.
class Worksheet(models.Model):
    team_name = models.CharField(max_length=100)
    project_name = models.CharField(max_length=100)
    working_on = models.CharField(max_length=100)
    work_status = models.CharField(max_length=20)
    entry_date = models.DateTimeField(default=datetime.now)
    description = models.TextField(blank=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic' )
    designation = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.user.username} Profile'

class Team(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User)
    def get_users(self):
        return ", ".join([user.username for user in self.users.all()])

    def __str__(self):
        return self.name

class Project(models.Model):
    project_status=(
        ("Finish","Finish"),
        ("Pending","Pending"),
        ("Started","Started"),
        ("In Discussion","In Discussion")
    )
    name = models.CharField(max_length=100, unique=True)
    team = models.CharField(max_length=100)
    project_status = models.CharField(max_length=100, choices = project_status, default=4)

    def __str__(self):
        return self.name

# class Workreport(models.Model):
#     project_name = models.OneToOneField(Project, on_delete=models.CASCADE)
#     team = models.OneToOneField(Team, on_delete=models.CASCADE)
#     date = models.DateTimeField(default=datetime.now)
#     user = models.ForeignKey(to=User, on_delete=models.CASCADE)
#     comment = models.TextField()
#     updated_by = models.CharField(max_length=100, blank=True)
    

#     def _get_login_user(request):
#         user = request.user
#         return user

#     def save(self, *args, **kwargs):
#         self.updated_by = self._get_login_user()
#         super(Workreport, self).save(*args, **kwargs)
class Workreport(models.Model):
    project_name = models.CharField(max_length=100, blank=True)
    team = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(default=datetime.now)
    user = models.CharField(max_length=100, blank=True)
    comment = models.TextField()
    updated_by = models.CharField(max_length=100, blank=True)
    

    def _get_login_user(request):
        user = request.user
        return user

    def save(self, *args, **kwargs):
        self.updated_by = self._get_login_user()
        super(Workreport, self).save(*args, **kwargs)
    