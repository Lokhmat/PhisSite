from django.conf.urls import url
from auth_user import views as login_views
from django.conf import settings
from django.urls import path,include

urlpatterns=[
	path('login', login_views.login,),
	path('register', login_views.register),
	path('logout', login_views.logout,)
]