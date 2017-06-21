from django.shortcuts import render, redirect
from .models import Books
# Create your views here.
def index(request):
    list = Books.objects.all()
    content = {
        'list': list
    }
    return render(request, 'full/index.html', content)

def submit(request):
    if request.method == "POST":
        Books.objects.create(title = request.POST['title'], category = request.POST['category'], author = request.POST['author'])
    return redirect("/")