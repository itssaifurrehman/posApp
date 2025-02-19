from django.contrib import admin  # ✅ Import this
from django.urls import path, include
from django.http import HttpResponse  # ✅ Import for a basic homepage

def home(request):
    return HttpResponse("Welcome to Django Home Page!")

urlpatterns = [
    path("admin/", admin.site.urls),  # ✅ Now admin is defined
    path("api/", include("api.urls")),  # Replace 'your_app' with your actual app name
    path("", home),  # Define a homepage route
]
