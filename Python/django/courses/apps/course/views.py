from django.shortcuts import render, redirect
from .models import Courses
# Create your views here.
def index(request):

    list = Courses.objects.all()
    content = {
        'list': list
    }
    return render(request, 'course/index.html', content)

def submit(request):
    if request.method == "POST":
        course = Courses.objects.create(name = request.POST['name'], description = request.POST['description'])


        return redirect("/")

def destroy(request, id):
    request.session['id'] = id
    course = Courses.objects.get(id = id)
    content = {
        'name': course.name,
        'description': course.description
    }
    return render(request, 'course/destroy.html', content)

def remove(request):
    Courses.objects.get(id = request.session['id']).delete()
    return redirect("/")

