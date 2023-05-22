from django.shortcuts import redirect, render, get_object_or_404
from .models import Task
from datetime import datetime
from .forms import TaskForm

# Create your views here.
def index_view(request):
    task = Task.objects.all()
    return render(request, 'index.html', context={'task': task})

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
            Task.objects.create(objective = objective, dead_line = date)
            return redirect('main')
        except ValueError:
            errors['date'] = "The following format required 'YYYY-MM-DD'"
            return render(request, 'new_task.html', context={'errors':errors})

# def list_task(request):


def detail_task(request, *args, **kwargs):
    task = get_object_or_404(Task,pk=kwargs.get('pk'))
    return render(request, 'detail_task.html', context = {'task': task})

def update_task(request, *args, **kwargs):
    task = get_object_or_404(Task, pk=kwargs.get('pk'))
    if request.method == 'GET': 
        return render(request, 'update_task.html', context = {'task': task})
    elif request.method == 'POST':

        objective = request.POST.get('objective')
        dead_line = request.POST.get('date')
        status = request.POST.get('status')

        task.objective = objective
        task.dead_line = dead_line
        # task.status = status
        task.save()
        print(task.objective)
        return redirect('main')

def delete_task(request, *args, **kwargs):
    task = get_object_or_404(Task, pk=kwargs.get('pk'))
    if 'delete_it' in request.POST:
        task.delete()
        return redirect('main')
    return render(request, 'delete_task.html', {'task': task})

# def delete_task(request, pk):
#     task = get_object_or_404(Task, pk=pk)

# def confirm_delete(request, pk):
#     task = get_object_or_404(Task, pk=pk)

#     if request.method == 'POST':
#         task.delete()
#         return redirect('main')

#     context = {'task': task}
#     return render(request, 'delete_task.html', context)
