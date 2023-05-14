from django.shortcuts import render, get_object_or_404
from .models import Task
from datetime import datetime
# from django.core.exceptions import ValidationError
# from django import forms

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
    errors = {}
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
        status = request.POST.get('status')
        date = request.POST.get('date')
        try:
            datetime.strptime(date, "%Y-%m-%d")
            Task.objects.create(objective = objective, status = status, dead_line = date)
            return render(request, 'list_task.html', context={'task': task})
        except ValueError:
            errors['date'] = "The following format required 'YYYY-MM-DD'"
            return render(request, 'new_task.html', context={'errors':errors})

def list_task(request):
    task = Task.objects.all()
    return render(request, 'list_task.html', context={'task': task})   

def detail_task(request, *args, **kwargs):
    task = get_object_or_404(Task,pk=kwargs.get('pk'))
    return render(request, 'detail_task.html', context = {'task': task})