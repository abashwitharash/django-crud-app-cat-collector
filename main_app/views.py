from django.shortcuts import render
from .models import Cat

def cat_index(request):
    cats = Cat.objects.all()  # look familiar?
    return render(request, 'cats/index.html', {'cats': cats})

# Define the home view function 
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cat_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'cats/detail.html', {'cat': cat})