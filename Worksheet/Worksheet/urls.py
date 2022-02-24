"""Worksheet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Worksheet_user import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', views.Dashboard, name='dashboard'),
    path('', views.WorkLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create_project/', views.createProject, name="create_project"),
    path('work_report/', views.workreport, name="work_report"),
    path('teamname', views.teamname, name="teamname"),
    path('createUser', views.createUser, name="createUser"),
    path('getuserlist/<int:id>',views.getuserlist, name='getuserlist'),
    path('works_status', views.workstatus, name="works_status" ),

    # Delete 
    path('deleteuser/<int:user_id>',views.deleteuser, name='deleteuser'),
    path('deleteteam/<int:team_id>',views.deleteteam, name='deleteteam'),
    path('deleteproject/<int:project_id>',views.deleteproject, name='deleteproject'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
