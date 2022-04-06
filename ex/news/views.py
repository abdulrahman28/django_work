from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {
        'name':'Abdul',
        'age':23,
        'email':'yusuf@gmail.com'
    }
    return render(request, 'index.html', context)

def counter(request):
    words = request.POST['text']
    words = len(words.split())
    context = {'words':words}
    return render(request, 'counter.html', context)