from django.shortcuts import render
from .models import Task

# Create your views here.
def index_view(request):
    return render(request,'index.html')

def new_task(request):
    if request.method == 'GET':
        return render(request,'new_task.html')
    elif request.method == 'POST':
        objective = request.POST.get('objective')
        status = 'new'
        date = request.POST.get('date')
        Task.objects.create(objective = objective, status = status, dead_line= date)

        return render(request, 'list_task.html')


def list_task(request):
    task = Task.objects.all()
    return render(request, 'list_task.html', context={'task': task})   