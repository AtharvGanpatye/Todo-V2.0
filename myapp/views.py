from django.shortcuts import render
from myapp.forms import UserForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from myapp.models import Todo

def index(request):

	context = {'name':'atharv'}
	return render(request, 'myapp/index.html')


def invalid_login(request):

	return render(request, 'myapp/invalid_login.html')


@login_required
def user_logout(request):

	logout(request)
	return HttpResponseRedirect(reverse('myapp:index'))


def register(request):

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)

		if user_form.is_valid():

			user = user_form.save()
			user.set_password(user.password)
			user.save()
			alert = 'Account Created Successfully ! Please Login'
			return render(request, 'myapp/login.html',{'alert':alert})

		else:
			print(user_form.errors)
	else:
		user_form = UserForm()

	return render(request, 'myapp/register.html', {'user_form':user_form})


def user_login(request):

	if request.method == 'POST':

		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('myapp:show_todos'))
			else:
				return HttpResponse("Account Not Active !")

		else:
			print("Invalid Login")
			print(username)
			print(password)

			return HttpResponseRedirect(reverse('myapp:invalid_login'))

	else:
		return render(request, 'myapp/login.html')


@login_required
def show_todos(request):

	user = request.user
	todos = user.todos.all()
	return render(request, 'myapp/show_todos.html',{'user':user, 'todos':todos})


@login_required
def delete_item(request, pk):

	if request.method == 'POST':
		user = request.user
		item_to_delete = user.todos.get(id=pk)
		item_to_delete.delete()
		return HttpResponseRedirect(reverse('myapp:show_todos'))


@login_required
def add_item(request):

	if request.method == 'POST':
		todo = request.POST.get('content')
		user = request.user
		if todo != '':
			item = Todo(owner=user, content=todo)
			item.save()

		return HttpResponseRedirect(reverse('myapp:show_todos'))