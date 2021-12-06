from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound

from .models import *
# Create your views here.
def index(request):
    return render(request, 'studhack/index.html')
    


def info(request, task_id):
    return HttpResponse(f"Info Page for Tasks: Task {task_id}")

def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=False)

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def index2(request):

    tasks = Tasks.objects.all()

    context = {
        'tasks' : tasks,
        # 'p1' : ' Lorem Ipsum Text',
        # 'p2' : 'tiny ipsum text'
    }
    return render(request, 'studhack/index2.html', context=context)

def index3(request):

    participants = Participants.objects.all()

    context = {
        'participants' : participants,
        # 'p1' : ' Lorem Ipsum Text',
        # 'p2' : 'tiny ipsum text'
    }
    return render(request, 'studhack/index3.html', context=context)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
