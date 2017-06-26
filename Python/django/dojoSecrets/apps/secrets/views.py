
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import User, Secret, Like

# Create your views here.
def index(request):
    list = User.objects.all()
    for i in list:
        print i.email
    return render(request, 'secrets/index.html')


def register(request):

    if request.method == "POST":
        values = User.objects.register(request.POST['first'], request.POST['last'], request.POST['email'], request.POST['password'], request.POST['confirm'])
        successful = True

        if values[0]:
            if not values[1]:
                messages.error(request, 'First Name can only contain letters and must have at least 2 characters')
                successful = False
            if not values[2]:
                messages.error(request, 'Last Name can only contain letters and must have at least 2 characters')
                successful = False
            if not values[3]:
                messages.error(request, 'Email is not valid')
                successful = False
            if not values[4]:
                messages.error(request, 'Password must be at least 8 characters')
                successful = False
            if not values[5]:
                messages.error(request, 'Passwords do not match')
                successful = False

            if successful:

                User.objects.create(first_name=request.POST['first'], last_name=request.POST['last'],
                                        email=request.POST['email'], password=request.POST['password'])
                request.session['first_name'] = request.POST['first']
                request.session['last_name'] = request.POST['last']
                return redirect('/secrets')
            else:
                return redirect('/')
        else:
            messages.error(request, 'User with email already exists')
            return redirect('/')


def login(request):
    if request.method == "POST":
        login = User.objects.login(request.POST['email'], request.POST['password'])
        print login
        if login[0]:
            request.session['first_name'] = login[1]
            request.session['last_name'] = login[2]
            # print request.session['last_name']
            return redirect('/secrets')
        else:
            messages.error(request, 'Email or password is incorrect')
            return redirect('/')

def secrets(request):
    content = {'name' : request.session['first_name']}
    return render(request, 'secrets/secrets.html', content)

def post(request):
    if request.method == "POST":
        secret = Secret.objects.create(content = request.POST['content'], user = User.objects.get(first_name = request.session['first_name'], last_name = request.session['last_name']))
        print secret.content
    return redirect('/secrets')