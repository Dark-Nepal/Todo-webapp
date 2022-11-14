from django.shortcuts import render
from datetime import datetime
from task.forms import TaskForm
from .models import Task


def home(request):

    return render(request,'home.html')

def addtask(request):
   if request.method == 'POST':
       filled_form = TaskForm(request.POST)
       if filled_form.is_valid():
           note = 'DeepAce your task is added !'
           filled_form.created = datetime.now()
           filled_form.save()
           newform = TaskForm()
           return render(request,'addtask.html',{'form' : newform,'note':note,})


   else:
        form = TaskForm()
        return render(request,'addtask.html', { 'form' : form,})

def task(request):

    tasks = Task.objects.filter(completed = False )

    return render(request,'task.html', {'tasks':tasks,})
