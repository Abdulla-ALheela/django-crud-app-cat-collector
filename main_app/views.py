# main_app/views.py

from django.shortcuts import render
from .models import Cat
# Import HttpResponse to send text-based responses


# Define the home view function
def home(request):
    # Send a simple HTML response
   return render(request, 'home.html')

# Define the about view function
def about(request):
    # Send a simple HTML response
  return render(request, 'about.html')


def cat_index(request):
    cats = Cat.objects.all()  # look familiar?
    return render(request, 'cats/index.html', {'cats': cats})


def cat_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'cats/detail.html', {'cat': cat})
