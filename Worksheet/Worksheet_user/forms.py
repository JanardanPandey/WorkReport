
from django import forms


from .models import Workreport, Worksheet, Team ,Project
from django.contrib.auth.models import User


class WorksheetForms(forms.ModelForm):
    class Meta:
        model = Worksheet
        fields = "__all__"
        widgets = {
        "team_name": forms.TextInput(
            attrs={
                "id":"team_id",
                "class":"form-control",
                "required":"true",
            }),
        "project_name": forms.TextInput(
            attrs={
                "class":"form-control",
                "id":"project_name"
            }),
        "working_on": forms.TextInput(
        attrs={
            "class":"form-control",
            "id":"working_on"
        }),
        "work_status": forms.TextInput(
        attrs={
            "class":"form-control",
            "id":"work_status"
        }),
        "entry_date": forms.TextInput(
        attrs={
            "class":"form-control",
            "id":"entry_date"
        }),
        "description": forms.TextInput(
        attrs={
            "class":"form-control",
            "id":"description"
        }),
        "user": forms.TextInput(
        attrs={
            "class":"form-control",
            "id":"user"
        }),
        }

    # class Widget:
    #     "team_name"=
    #     project_name
    #     working_on
    #     work_status
    #     entry_date
    #     description
    #     user
# class ValidateProjectForm(forms.Form):
#     name = forms.CharField()
#     team = forms.CharField()
#     project_status = forms.CharField()

    
class ValidateProjectForm(forms.ModelForm):
    # project_status_choice=(
    #     ("Finish","Finish"),
    #     ("Pending","Pending"),
    #     ("Started","Started"),
    #     ("In Discussion","In Discussion")
    # )
    # name = forms.CharField(label ="Project Name", max_length=100)
    team = forms.ModelChoiceField(queryset = Team.objects.all(), label="Team")
    # project_status =forms.ChoiceField(choices=project_status_choice, label="Project Status")
    class Meta:
        model= Project
        fields=["name", "team","project_status"]
        # fields = '__all__'
        widgets = {
        "name": forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Project Name"
            }),
        "team": forms.Select(
            attrs={
                "class":"form-control",
            }),
        "project_status": forms.Select(
            attrs={
                "class":"form-control",
            }),
        }


class WorkReportForm(forms.ModelForm):
    project_name = forms.ModelChoiceField(queryset=Project.objects.all())
    team = forms.ModelChoiceField(queryset=Team.objects.all(), widget=forms.Select(attrs={'class':'form-control','onchange':'userlist(this)'}))
    user = forms.ModelChoiceField(queryset=User.objects.all())
    # comment=forms.CharField(max_length=100)
    class Meta:
        model=Workreport
        fields = ["project_name","team","user","comment"]
        widgets = {
        "team": forms.Select(
            attrs={
                "class":"form-control",
                "placeholder":"Team Name",
                "onchange":"userlist(this)"
            })
        }

class TeamNameForm(forms.ModelForm):
    # user = forms.ModelChoiceField(queryset=Team.objects.get("users"))
    class Meta:
        model = Team
        fields = '__all__'


class UserCreateForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "password" ]
