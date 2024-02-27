from django.contrib import admin
from django.urls import path, include  # Correctly imported 'include' here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hello.urls')),  # Assuming 'hello' is the name of your app
]
