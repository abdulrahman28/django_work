from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.

def index(request):


    features = Feature.objects.all()

    context = {
        'name':'Abdul',
        'age':23,
        'email':'yusuf@gmail.com',
        'features':features,
    }
    return render(request, 'index.html', context)

def register(request):
    if request.method == 'POST':
        passw = request.POST['pass']
        cpassw = request.POST['cpass']
        if passw == cpassw:
            user = request.POST['user']
    

    return render(request, 'register.html')


def login(request):

    return render(request, 'register.html')


def counter(request):
    words = request.POST['text']
    words = len(words.split())
    context = {'words':words}
    return render(request, 'counter.html', context)