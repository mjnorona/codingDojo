import random, string
from django.shortcuts import render

# Create your views here.
def index(request):
    if "count" in request.session:
        request.session['count'] +=1
    else:
        request.session['count'] = 1
    data = {
        'word': ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(14)])
    }
    return render(request, "randomWord/index.html", data)