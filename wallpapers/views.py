from django.shortcuts import render, get_object_or_404
from .models import Wallpaper

def home(request):
    wallpapers = Wallpaper.objects.all()

    search_query = request.GET.get('q','').strip()
    category = request.GET.get('category','').strip()

    if search_query:
        wallpapers = wallpapers.filter(
            title__icontains=search_query
        )

    if category:
        wallpapers = wallpapers.filter(
            category=category
        )

    categories = Wallpaper.Category.choices

    context = {
        'wallpapers': wallpapers,
        'categories': categories,
        'search_query': search_query,
        'search_category': category,
        'total_wallpapers': wallpapers.objects.count(),
    }

    return render(request, 'home.html', context)

def wallpaper_detail(request, pk):
    wallpaper = get_object_or_404(Wallpaper, pk=pk)

    related_wallpapers = Wallpaper.objects.filter(
        category=wallpaper.category,
    ).exclude(pk=wallpaper.pk)[:8]

    context = {
        'wallpaper': wallpaper,
        'related_wallpapers': related_wallpapers,
    }

    return render(
        request,
        'wallpaper_detail.html',
        context
    )