import random
from django.shortcuts import render,redirect
VALUES = ['phone', 'laptop', 'tablet', 'tv', 'xbox', 'guitar', 'microphone']
# Create your views here.
def index(request):
    return render(request, 'surprise/index.html')

def process(request):
    if request.method == "POST":
        request.session['number'] = int(request.POST['number'])
        return redirect('/results')
    else:
        return redirect("/")

def shuffle(list):
    for i in range(len(list)-1, 0, -1):
        number = random.randint(0, i)
        temp = list[i]
        list[i] = list[number]
        list[number] = temp

def results(request):
    try:
        vals = []
        shuffle(VALUES)
        for i in range(0, request.session['number']):
            vals.append(VALUES[i])

        content = {
            'items': vals
        }
    except IndexError:
        return redirect('/')

    return render(request, 'surprise/results.html', content)