from django.contrib import admin
from .models import  Wallpaper

@admin.register(Wallpaper)
class WallpaperAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'category',
        'device_type',
        'resolution',
        'downloads',
        'is_featured',
        'created_at',
    )

    list_filter = (
        'category',
        'device_type',
        'is_featured',
    )

    search_fields = ('title','description')

    list_editable = ('is_featured',)

    readonly_fields = ('created_at', 'downloads')