from django.contrib import admin
from Worksheet_user.models import Worksheet, Profile, Team , Project , Workreport

# Register your models here.
admin.site.register(Worksheet)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
        list_display = ['user', 'profile_pic', 'user']

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display=['name',"get_users"]

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name','team']

@admin.register(Workreport)
class WorkreportAdmin(admin.ModelAdmin):
    list_display=['project_name','date','comment','user','updated_by']