from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Destination, Booking

# --- Existing views ---
def home(request):
    destinations = Destination.objects.all()
    return render(request, 'travelworld/home.html', {'destinations': destinations})

def destination_detail(request, id):
    destination = get_object_or_404(Destination, id=id)
    return render(request, 'travelworld/destination_detail.html', {'destination': destination})

@login_required(login_url='login')
def book_destination(request, destination_id):
    destination = get_object_or_404(Destination, id=destination_id)

    if request.method == "POST":
        persons = request.POST.get('persons')

        Booking.objects.create(
            user=request.user,
            destination=destination,
            persons=persons
        )

        return redirect('my_bookings')

    return render(request, 'travelworld/book_destination.html', {'destination': destination})

@login_required(login_url='login')
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'travelworld/my_bookings.html', {'bookings': bookings})

# --- ✅ New Registration View ---
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()       # Save the new user
            login(request, user)     # Automatically log in the user
            return redirect('home')  # Redirect to home page
    else:
        form = UserCreationForm()
    return render(request, 'travelworld/register.html', {'form': form})
