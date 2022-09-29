from django.shortcuts import render
from todolist.models import Task
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TaskForm

@login_required(login_url='/todolist/login/')
# Create your views here.
def show_todolist(request):
    data_todolist = Task.objects.all()
    context = {
        'todolist': data_todolist,
        'nama': 'Hanin',
        'student_id': '2106751234',
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

def get_task(request):
    form = TaskForm()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TaskForm(request.POST)
        title = request.POST.get('title')
        description = request.POST.get('description')

        # check whether it's valid:
        if form.is_valid():
            task = Task()
            # process the data in form.cleaned_data as required
            task.user = request.user
            task.date = datetime.datetime.now()
            task.title = form.cleaned_data['title']
            task.description = form.cleaned_data['description']
            task.save()
            # redirect to a new URL:
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            return response

    # if a GET (or any other method) we'll create a blank form
        
    return render(request, 'createTask.html', {'form':form})