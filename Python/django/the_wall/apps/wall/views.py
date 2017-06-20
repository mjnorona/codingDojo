import re, md5, os, binascii
from django.shortcuts import render, redirect
from .models import Users, Messages, Comments
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your views here.

def hasNumbers(input):
    for i in input:
        if i.isdigit():
            return True
    return False

def index(request):
    return render(request, 'wall/index.html')

def register(request):
    if request.method == "POST":
        if request.POST['action'] == 'register':
            if (hasNumbers(request.POST['first']) == False and len(request.POST['first']) >= 2
                and hasNumbers(request.POST['last']) == False and len(request.POST['last']) >= 2
                and EMAIL_REGEX.match(request.POST['email']) and request.POST['email'] > 0
                and len(request.POST['password']) >= 8 and request.POST['password'] == request.POST['confirm']):
                print "Correct"
            else:
                print "Not Correct"
    return redirect("/")




