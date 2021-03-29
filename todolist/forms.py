from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"

        title = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder": "Enter task...",
                }
            ),
    )
    completed = forms.CharField(
        required=False,
        widget=forms.widgets.CheckboxInput(
            attrs={"class": "form-check-input"}
        ),
    )

class CreateUserForm(UserCreationForm):
    class Meta:
         model = User
         fields = ['username','email', 'password1', 'password2']