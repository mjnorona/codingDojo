import random, time
from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    return render(request, 'ninja/index.html')

def process(request):
    thisisdate = time.asctime(time.localtime(time.time()))
    if request.POST['action'] == 'farm':
        number = random.randrange(10, 21)
        request.session['gold'] += number
        request.session['activities'].append("Earned " + str(number) + " golds from the farm! " + thisisdate)
        return redirect('/')
    elif request.POST['action'] == 'cave':
        number = random.randrange(5, 11)
        request.session['gold'] += number
        request.session['activities'].append("Earned " + str(number) + " golds from the cave! " + thisisdate)
        return redirect('/')
    elif request.POST['action'] == 'house':
        number = random.randrange(2, 6)
        request.session['gold'] += number
        request.session['activities'].append("Earned " + str(number) + " golds from the house! " + thisisdate)
        return redirect('/')
    else:
        number = random.randrange(2, 6)
        takeOrNot = random.randrange(0, 2)
        if takeOrNot == 0:
            request.session['gold'] -= number
            request.session['activities'].append(
                "Entered a casino and lost  " + str(number) + " golds... Ouch... " + thisisdate)
            return redirect('/')
        else:
            request.session['gold'] += number
            request.session['activities'].append("Earned " + str(number) + " golds from the casino! " + thisisdate)
            return redirect("/")

def reset(request):
    request.session['gold'] = 0
    request.session['activities'] = []
    return redirect('/')