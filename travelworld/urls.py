from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('destination/<int:id>/', views.destination_detail, name='destination_detail'),

    # ✅ Booking URLs
    path('book/<int:destination_id>/', views.book_destination, name='book_destination'),
    path('mybookings/', views.my_bookings, name='my_bookings'),

    # ✅ Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='travelworld/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),  # We'll create this view next
]
