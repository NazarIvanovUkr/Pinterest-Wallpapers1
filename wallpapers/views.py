from django.shortcuts import render
from .models import Wallpaper

def home(request):
    wallpapers = Wallpaper.objects.all()

    context = {
        'wallpapers': wallpapers,
    }
    return render(request, 'home.html', context)
# Create your views here.
