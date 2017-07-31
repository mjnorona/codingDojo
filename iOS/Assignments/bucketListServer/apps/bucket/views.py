from django.shortcuts import render, HttpResponse
from django.core import serializers
from .models import Task

from django.views.decorators.csrf import csrf_exempt
import json
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.
def index(request):
    Task.objects.all().delete()
    return render(request, 'bucket/index.html')

@csrf_exempt
def tasks(request):
    if request.method == "GET":
        data = serializers.serialize('json', Task.objects.all())
        return HttpResponse(data, content_type = 'application/json')
    elif request.method == "POST":
        print("Request: ", request.POST)
        item = Task.objects.create(objective = request.POST["objective"])
        data = serializers.serialize('json',Task.objects.filter(id = item.id))
        

        return HttpResponse(data, content_type = 'application/json')

@csrf_exempt        
def update(request):
    if request.method == "POST":
        print("Request: ", request.POST)
        task = Task.objects.get(id = request.POST['id'])
        task.objective = request.POST['objective']
        task.save()
        data = serializers.serialize('json', task)
        

        return HttpResponse(data, content_type = 'application/json')

def delete(request):
    return "goodbye"