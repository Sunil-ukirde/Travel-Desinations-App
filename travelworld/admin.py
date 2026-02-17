from django.contrib import admin
from .models import Destination, Booking

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration', 'rating')
    list_filter = ('best_time',)
    search_fields = ('name', 'tagline')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'destination', 'persons', 'booking_date')
    list_filter = ('destination', 'booking_date')
    search_fields = ('user__username', 'destination__name')
