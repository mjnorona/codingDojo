from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "port/index.html")

def projects(request):
    return render(request, "port/projects.html")

def about(request):
    return render(request, "port/about.html")

def test(request):
    return render(request, "port/testimonials.html")

