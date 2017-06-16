from django.shortcuts import render
#CONTROLLER
# Create your views here.
from django.shortcuts import render, HttpResponse


# the index function is called when root is visited
def index(request):
    print ("*" * 100)
    return render(request, 'first_app/index.html')