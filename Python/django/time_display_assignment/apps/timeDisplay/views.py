import datetime
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    time = datetime.datetime.now()
    data = {
        'time': time
    }
    return render(request, "timeDisplay/index.html", data)