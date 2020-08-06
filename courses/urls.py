from django.conf.urls import url
from . import views
from django.conf import settings
from django.urls import path,include

urlpatterns=[
	path('',views.course),
	path('/<int:idvar>', views.course_one),
]