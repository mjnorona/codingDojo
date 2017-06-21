from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usernames

# Create your views here.
def index(request):
    return render(request, 'validation/index.html')

def submit(request):
    if request.method == "POST":
        if len(request.POST['username']) < 8 or len(request.POST['username']) > 26:
            messages.error(request, 'Username is not valid!')
            return redirect("/")
        else:
            request.session['username'] = request.POST['username']
            Usernames.objects.create(username = request.POST['username'])
            return redirect('/success')

def success(request):
    print request.session['username']
    messages.success(request, "The username you entered " + request.session['username'] + " is valid. Thank You!")
    usernames = Usernames.objects.all()
    content = {'usernames': usernames}
    return render(request, 'validation/success.html', content)
