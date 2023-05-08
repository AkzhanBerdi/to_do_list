from django.shortcuts import render
from .models import Task
from django.core.exceptions import ValidationError
from django import forms

# class InvalidDateFormatError(ValidationError):
#     pass

# class TaskForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = ['objective', 'status', 'dead_line']

# Create your views here.
def index_view(request):
    return render(request,'index.html')

def new_task(request):
    choices = [
        ('New', 'New'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]
    if request.method == 'GET':
        return render(request,'new_task.html',{'choices': choices})
    elif request.method == 'POST':
        task = Task.objects.all()
        objective = request.POST.get('objective')
        status = 'new'
        date = request.POST.get('date')
        Task.objects.create(objective = objective, status = status, dead_line = date)

        return render(request, 'list_task.html', context={'task': task})

def list_task(request):
    task = Task.objects.all()
    return render(request, 'list_task.html', context={'task': task})   