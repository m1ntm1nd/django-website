from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *
# from .utils import *

def index(request):
    return render(request, 'studhack/index.html')
    


def info(request, task_id):
    return HttpResponse(f"Info Page for Tasks: Task {task_id}")

def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=False)

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def tasks(request):

    tasks = Tasks.objects.all()
    teamsquery = []
    for item in tasks:
        teamsquery.append(Teams.objects.filter(task_id=item.id))
    teamsquery = teamsquery[::-1]

    context = {
        'tasks' : tasks,
        'teamsquery' : teamsquery
        # 'p1' : ' Lorem Ipsum Text',
        # 'p2' : 'tiny ipsum text'
    }
    return render(request, 'studhack/tasks.html', context=context)

def parts(request):

    participants = Participants.objects.all()
    participantsF = participants.filter(team_id=1)
    context = {
        'participants' : participants,
        'participantsF' : participantsF,
        # 'p1' : ' Lorem Ipsum Text',
        # 'p2' : 'tiny ipsum text'
    }
    return render(request, 'studhack/parts.html', context=context)

def teams(request):

    teams = Teams.objects.all()
    partsquery = []
    for item in teams:
        partsquery.append(Participants.objects.filter(team_id=item.id))
    partsquery = partsquery[::-1]
    context = {
        'teams' : teams,
        'participants' : partsquery,
        # 'p1' : ' Lorem Ipsum Text',
        # 'p2' : 'tiny ipsum text'
    }
    return render(request, 'studhack/teams.html', context=context)

def login(request):


    
    return render(request, 'studhack/register.html')



# def register(request):

#     # if request.method == 'POST':
#     #     form = AddRegistrationForm(request.POST)
#     #     if form.is_valid():
#     #         print(form.cleaned_data)
#     #         try:
#     #             #Users.objects.create(**form.cleaned_data)
#     #             return redirect('home')
#     #         except:
#     #             form.add_error(None, 'Ошибка добавления поста')
#     # else:
#     #     form = AddRegistrationForm(request.POST)

    
#     return render(request, 'studhack/register.html')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'studhack/register.html'
    success_url = reverse_lazy('login')

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     c_def = self.get_user_context(title="Регистрация")
    #     return dict(list(context.items()) + list(c_def.items()))
