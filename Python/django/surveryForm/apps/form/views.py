from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, 'form/index.html')

def result(request):

    return render(request, "form/result.html")

def process(request):
    print(request.method)
    if request.method == "POST":
        print('*' * 50)
        print (request.POST)
        print ('*' * 50)
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        return redirect("/result")
    else:
        return redirect("/")