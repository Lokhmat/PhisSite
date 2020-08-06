from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from Main.models import form, zadachi, foruser, courses, Student
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def login(request):
	context = {}
	if request.method == "POST":
		username = request.POST.get('username',"")
		password = request.POST.get('password',"")
		user = auth.authenticate(username = username, password = password)
		if user is not None:
			auth.login(request,user)
			return HttpResponseRedirect('/')
		else:
			error = "Oh!"
			context = {'error': error}
			return render(request,'go/loginpage.html', context)
	else:
		return render(request, 'go/loginpage.html', context)

def register(request):
	context = {}
	register_form = UserCreationForm()
	context = {"register_form": register_form}
	if request.method == "POST":
		new_user_form = UserCreationForm(request.POST)

		if new_user_form.is_valid():
			ids = User.objects.all()
			t=[]
			for e in ids:
				t.append(e.id)
			curr_id = int(max(t)+1)
			
			
			new_user_form.save()
			new_user = auth.authenticate(username=new_user_form.cleaned_data['username'],password=new_user_form.cleaned_data['password2'])
			c = str(new_user_form.cleaned_data['username'])
			person = foruser(login=c,zadachi='',teachers='', olimps='')
			person.save()
			
			person1 = Student(done_tasks='', ava='[2]',user_id=curr_id)
			person1.save()
			auth.login(request, new_user)
			return HttpResponseRedirect('/')

		else:
			register_form = new_user_form
			context = {"register_form": register_form}
	return render(request, 'go/register.html', context)

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')