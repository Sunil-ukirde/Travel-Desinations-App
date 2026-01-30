from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Destination

def home(request):
    destinations = Destination.objects.all()
    return render(request, 'travelworld/home.html', {'destinations': destinations})

def destination_detail(request, id):
    destination = get_object_or_404(Destination, id=id)
    return render(request, 'travelworld/destination_detail.html', {'destination': destination})
