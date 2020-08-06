# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import form, zadachi, foruser, courses, Student
from django.views.generic.edit import FormView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.views.generic import ListView, DetailView

# Create your views here.

def bot(request):
	return render(request, 'Main/botUI.html')

def index(request):
    username = auth.get_user(request).username
    return render(request, 'Main/homepage.html', {'username': username})


def lib(request):
    username = auth.get_user(request).username
    book = form.objects.all()
    object_list = []
    object_list = form.objects.all()

    return render(request, 'Main/lib.html', context={'username': username, 'list': object_list})


def lich(request):
    username = auth.get_user(request).username
    tasks = foruser.objects.all()
    user_id = auth.get_user(request).id
    done = Student.objects.filter(user_id=user_id)
    ava = Student.objects.filter(user_id=user_id)
    k = ''
    img = '[2]'
    for e in ava:
        img = e.ava
    for e in done:
        k = e.done_tasks
    ko = []
    ko = k.split('|')
    p = set(ko)
    l = ''
    for e in p:
        l = l+str(e)+' '

    print(l)
    return render(request, 'Main/lich.html', context={'username': username, 'tasks': tasks, 'done': l, 'ava': img})


def tasks(request):
    object_list = []
    object_list = zadachi.objects.all()
    username = auth.get_user(request).username
    return render(request, 'Main/tasks.html', context={'username': username, 'object_list': object_list})


def course(request):
    object_list = []
    object_list = courses.objects.all()
    username = auth.get_user(request).username
    return render(request, 'Main/courses.html', context={'object_list': object_list, 'username': username})


def program(request):
    username = auth.get_user(request).username
    return render(request, 'Main/prog_page.html', context={'username': username})


def olimp(request):
    username = auth.get_user(request).username
    tasks = []
    tasks = zadachi.objects.filter(tags='Chern')
    
    return render(request, 'Main/chern.html', context={'username': username, 'tasks': tasks})


def belolip(request):

    username = auth.get_user(request).username
    tasks = []
    tasks = zadachi.objects.filter(tags='Belolip')
    
    tasks1=[]
    tasks2=[]
    tasks3=[]
    tasks4=[]
    tasks5=[]
    tasks6=[]
    for e in tasks:
        print(e.name,e.text)
        if 'Б1'in e.name:
            tasks1.append(e)
        elif 'Б2'in e.name:
            tasks2.append(e)
        elif 'Б3'in e.name:
            tasks3.append(e)
        elif 'Б4'in e.name:
            tasks4.append(e)
        elif 'Б5'in e.name:
            tasks5.append(e)
        elif 'Б6'in e.name:
            tasks6.append(e)
            
    
    return render(request, 'Main/belolip.html', context={'username': username,'tasks':tasks, 'tasks1': tasks1,'tasks2': tasks2,'tasks3': tasks3,'tasks4': tasks4,'tasks5': tasks5,'tasks6': tasks6})
    


def chern(request):
    username = auth.get_user(request).username

    return render(request, 'Main/chern.html', context={'username': username})


def task_one(request, pk):
    username = auth.get_user(request).username
    object_list = []
    object_list = zadachi.objects.all()
    user_id = auth.get_user(request).id
    p = request
    p = str(p)
    s = []
    s = p.split('/')
    p = s[len(s)-1]
    p = int(p[:len(p)-2])

    temp = zadachi.objects.filter(id=p)
    for e in temp:
        c = e.text
        ans_g = e.answer
    print(c)
    b = True
    
    if c[0]=='=':
    	b = True
    else:
    	b = False

    if not(str(ans_g[0]) == '@'):
        y = True
    else:
        y = False
    if request.method == "POST":
        if user_id != None:
            ans_p = request.POST.get('answer', "")

            if ans_p == ans_g:

                p = '|'+str(p)

                d_t = Student.objects.filter(user_id=user_id)
                for e in d_t:
                    d_t_t = e.done_tasks
                d_t_g = str(d_t_t) + str(p)
                print(d_t_g)

                curr = Student.objects.filter(user_id=user_id)

                for e in curr:
                    e.done_tasks = d_t_g
                    e.save()

                context = {'username': username, 'object_list': object_list,
                           'task_id': int(p[1:]), 'error': "Правильно!", 'b': b, 'y':y}
                return render(request, 'Main/task_one.html', context)
            else:
                context = {'username': username, 'object_list': object_list,
                           'task_id': p, 'error': "Неправильно!", 'b': b, 'y':y}
                return render(request, 'Main/task_one.html', context)
        else:
            context = {'username': username, 'object_list': object_list, 'task_id': p,
                       'error': 'Войдите, чтобы решать задачи', 'b': b, 'y':y}
            return render(request, 'Main/task_one.html', context)

    else:
        if user_id != None:
            done = []
            print(user_id)
            d_t = Student.objects.filter(user_id=user_id)
            for e in d_t:
                d_t_t = e.done_tasks

            done = str(d_t_t).split('|')

            if str(p) in done:
                context = {'username': username, 'object_list': object_list, 'task_id': p,
                           'error': 'Вы уже сделали эту задачу правильно, ваш ответ: ' + str(ans_g), 'b': b, 'y':y}
                return render(request, 'Main/task_one.html', context)
            else:
                context = {'username': username,
                           'object_list': object_list, 'task_id': p, 'b': b, 'y':y}
                return render(request, 'Main/task_one.html', context)
        else:
            context = {'username': username, 'object_list': object_list, 'task_id': p,
                       'error': 'Войдите, чтобы решать задачи', 'b': b, 'y':y}
            return render(request, 'Main/task_one.html', context)


def red(request):
    username = auth.get_user(request).username
    context = {'username': username}
    return render(request, 'Main/red.html', context)
