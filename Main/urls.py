from django.urls import path, include
from . import views
from django.views.generic import ListView, DetailView
from .models import form, zadachi
from django.conf.urls import url

urlpatterns = [
    path('', views.index),
    path('lib', views.lib),
    path('lich', views.lich),
    path('bot', views.bot),
    path('prog', views.program),
    path('tasks', views.tasks),
    path('olimp',views.olimp),
    path('belolip',views.belolip),
    path('chern',views.chern),
    #path('course', views.course),
    #url('(?P<pk>\d+)', views.task_one),
    path('<int:pk>', views.task_one),
    path('red',views.red),
]
