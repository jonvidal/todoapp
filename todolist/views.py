from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import TaskForm, CreateUserForm
from .models import Task


def registerPage(request):
    form =  CreateUserForm()

    if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')

    context =  {'form':form}
    return render(request, 'accounts/register.html', context)

def index(request):
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")

    tasks = Task.objects.all()
    return render(request, "index.html", {"task_form": form, "tasks": tasks})

def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form =  TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("index")  
    return render(request, "update_task.html",  {"task_edit_form": form})

def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect("index")