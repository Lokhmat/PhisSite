from django.shortcuts import render
from .models import Course, Teo
from Main.models import zadachi, Student
from django.views.generic.edit import FormView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.views.generic import ListView, DetailView
# Create your views here.


def course(request):
    object_list = []
    object_list = Course.objects.all()
    username = auth.get_user(request).username

    return render(request, 'courses/courses.html', context={'object_list': object_list, 'username': username})


def course_one(request, idvar):
    b = False
    username = auth.get_user(request).username
    user_id = auth.get_user(request).id
    d_t = Student.objects.filter(user_id=user_id)
    for e in d_t:
        d_t_t = e.done_tasks

        done = str(d_t_t).split('|')
    
    if user_id != None:
        b=True
    tasks = []
    kost = []
    object_list = []
    cour = Course.objects.filter(id=idvar)
    for e in cour:
        name = e.blocks
    names = []
    names = name.split('|')
    for e in cour:
        inner = e.blocks_inner
    inner_bl = []
    inner_b = []
    inner_b = inner.split('|')
    for i in range(len(names)):
        inner_bl.append([names[i], ])

    for i in range(len(inner_bl)):
        object_list = []
        object_list = inner_b[i].split('+')
        for j in object_list:
            inner_bl[i].append(j)
    img_id = []

    for i in range(len(inner_bl)):
        for j in range(len(inner_bl[i])):
            if 'teo:' in inner_bl[i][j]:
                id = inner_bl[i][j][4:]
                teo = Teo.objects.filter(id=id)
                for e in teo:
                    teoret = e.text
                inner_bl[i][j] = {'name': teoret}
                kost.append(teoret)
            elif 'pr:' in inner_bl[i][j]:
                id = inner_bl[i][j][3:]
                zad = zadachi.objects.filter(id=id)
                for e in zad:
                    kek = e.name
                inner_bl[i][j] = {'name': str(str(id)+'.'+str(kek)), 'id': id}
                tasks.append(str(str(id)+'.'+str(kek)))
            elif 'img:' in inner_bl[i][j]:
                temp = inner_bl[i][j][4:]
                inner_bl[i][j] = {'name':inner_bl[i][j][4:]}
                img_id.append(temp)
            elif inner_bl[i][j] not in names:
                temp = inner_bl[i][j]
                inner_bl[i][j] = {'name': temp}
                kost.append(temp)
            else:
                inner_bl[i][j] = {'name': inner_bl[i][j]}

    context = {'blocks': names, 'inner_blocks': inner_bl,
               'num': len(names), 'tasks': tasks, 'kost': kost, 'img_id': img_id, 'flag':b, 'username':username,'done':done}
    return render(request, 'courses/course_one.html', context=context)
