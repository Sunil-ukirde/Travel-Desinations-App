from django.db import models
from django.contrib.auth.models import User


class Destination(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='destinations/')

    highlights = models.TextField(max_length=1000, default="Beautiful destination")
    best_time = models.CharField(max_length=100, default="Not specified")
    duration = models.CharField(max_length=50, default="3 Days")
    rating = models.FloatField(default=4.5)

    def get_highlights_list(self):
        return self.highlights.split('\n')

    def __str__(self):
        return self.name


# ✅ MAKE SURE THIS CLASS EXISTS
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    persons = models.IntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.destination.name}"
