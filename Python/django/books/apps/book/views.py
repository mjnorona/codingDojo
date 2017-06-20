from django.shortcuts import render
from .models import Books
# Create your views here.
def index(request):

    return render(request, 'book/index.html')