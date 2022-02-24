from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from .forms import WorksheetForms , ValidateProjectForm, WorkReportForm, TeamNameForm, UserCreateForm
from django.contrib.auth.views import LoginView
from .import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test, login_required

@login_required
def Dashboard(request):
    worksheets = models.Worksheet.objects.all()
    total_projects = models.Project.objects.all().count()
    total_teams = models.Team.objects.all().count()
    total_users = models.User.objects.all().count()
    workreport = models.Workreport.objects.all()
    team_list = models.Team.objects.all()
    context ={
        'total_teams':total_teams,
        'worksheets': worksheets , 
        'total_projects':total_projects,
        'total_users':total_users,
        "workreport":workreport,
        "teams":team_list
    }
    return render(request,'main/index.html', context)


class WorkLoginView(LoginView):
    template_name = 'main/login.html'

@login_required
def workstatus(request):
    workreport = models.Workreport.objects.all()
    team_list = models.Team.objects.all()
    context ={
        "workreport":workreport,
        "teams":team_list
    }
    return render(request, 'main/works_status.html', context)


@login_required
def worksheet_dashboard(request):
    return render(request, 'main/work_upload.html', {"form":WorksheetForms})

@login_required
def createProject(request):
    if request.method=="POST":       
        fm = ValidateProjectForm(request.POST)
        print(fm)
        if fm.is_valid():
            try:
                obj = models.Project.objects.get(name=fm.cleaned_data["name"])
                return redirect("/create_project")
            except:
                
                
                # obj = models.Project(name=fm.cleaned_data["name"],team=fm.cleaned_data["team"],project_status=fm.cleaned_data["project_status"])
                fm.save()
                messages.success(request, " saved")
                return redirect("/create_project")
        projects = models.Project.objects.all()
        messages.error(request, request.POST["name"]+ " already exist")
        return render(request, "main/project.html",{"form":ValidateProjectForm,"project":projects})
    projects = models.Project.objects.all()
    return render(request, "main/project.html",{"form":ValidateProjectForm, "project":projects})

@login_required
def workreport(request):
    workreport = models.Workreport.objects.all()
    if request.method=="POST": 
        fm = WorkReportForm(request.POST)
        print("form data")
        if fm.is_valid():
            fm.save()
            return redirect("/work_report")
        print("here")
        return render(request,"main/workreport.html", {"form":WorkReportForm, "workreport":workreport })
    return render(request, "main/workreport.html", {"form":WorkReportForm, "workreport":workreport})

@login_required
def teamname(request):
    if request.method=="POST":
        fm = TeamNameForm(request.POST)        
        if fm.is_valid():
            print(fm)
            fm.save()
            return redirect("/teamname")
        return redirect("/teamname")
    teams = models.Team.objects.all()
    return render(request, "main/teams.html", {"form":TeamNameForm, "teams":teams})


def is_superuser(user):
    print('USer passes')
    return user.is_superuser

@login_required
@user_passes_test(is_superuser)
def createUser(request):
    user_list = User.objects.filter(is_superuser = False)
    if request.method=='POST':
        fm = UserCreateForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect("/createUser")
    return render(request, "main/create_user.html", {"form":UserCreateForm,'user_list':user_list})

from django.http import JsonResponse
@login_required
def getuserlist(request, id:int):
    get_team_user = models.Team.objects.get(id=id)
    print(get_team_user.users.all())
    context = {}
    for i in get_team_user.users.all():
        print(i.id)
        context[i.id]=i.username
    print(context)
    
    # userList = models.Team.objects.get(team = get_team_user)
    # print(userList)
    return JsonResponse(context)

@login_required  
def deleteuser(request,user_id):
    usr_dlt = User.objects.get(id=user_id)
    usr_dlt.delete()
    return redirect('createUser')

@login_required  
def deleteteam(request,team_id):
    team_dlt = models.Team.objects.get(id=team_id)
    team_dlt.delete()
    return redirect('teamname')


@login_required  
def deleteproject(request,project_id):
    project_dlt = models.Project.objects.get(id=project_id)
    project_dlt.delete()
    return redirect('create_project')