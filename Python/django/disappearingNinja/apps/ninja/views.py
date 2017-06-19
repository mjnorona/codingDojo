from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'ninja/index.html')

def tmnt(request):
    return render(request, 'ninja/ninja.html')

def color(request, color):
    ninja = ""
    if color == 'purple':
        ninja = 'donatello'
    elif color == 'blue':
        ninja = 'leonardo'
    elif color == 'red':
        ninja = 'raphael'
    elif color == 'orange':
        ninja = 'michelangelo'
    else:
        ninja = 'notapril'

    context = {
        'ninja': ninja
    }
    return render(request,'ninja/certainNinja.html', context)