from django.urls import path, include  # Make sure to include 'include' here
from .views import hello_world

urlpatterns = [
    path('', hello_world, name='hello_world'),
]