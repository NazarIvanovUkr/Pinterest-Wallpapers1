from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path(
        'wallpaper/<int:pk>/',
        views.wallpaper_detail,
        name='wallpaper_detail'
    ),
]
