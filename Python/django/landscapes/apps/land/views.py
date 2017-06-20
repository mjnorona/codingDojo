from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'land/index.html')

def land(request, number):
    value = int(number)
    if value <=50:
        picture = ''
        if value >= 1 and value <= 10:
            picture = 'snow'
        elif value >=11 and value <= 20:
            picture = 'desert'
        elif value >=21 and value <= 30:
            picture = 'forest'
        elif value >= 31 and value <= 40:
            picture = 'vineyard'
        elif value >= 41 and value <= 50:
            picture = 'tropical'

        content = {
            'picture': picture
        }
        return render(request, 'land/landscapes.html', content)
    else:
        return redirect("/")