#wallpapers/models.py
from django.db import models


class Wallpaper(models.Model):

    class Category(models.TextChoices):
        GAMING = 'gaming', 'Gaming'
        TECHNOLOGY = 'tech', 'Technology'
        MEMES = 'memes', 'Memes'
        NATURE = 'nature', 'Nature'
        ANIME = 'anime', 'Anime'
        ABSTRACT = 'abstract', 'Abstract'
        CARS = 'cars', 'Cars'
        SPACE = 'space', 'Space'
        MINIMAL = 'minimal', 'Minimal'
        OTHER = 'other', 'Other'

    class DeviceType(models.TextChoices):
        PC = 'pc', 'PC'
        MOBILE = 'mobile', 'Mobile'
        TABLET = 'tablet', 'Tablet'
        DUAL = 'dual', 'Dual Monitor'

    title = models.CharField(
        max_length=150,
        verbose_name='Назва'
    )

    image = models.ImageField(
        upload_to='wallpapers/',
        verbose_name='Зображення'
    )

    category = models.CharField(
        max_length=20,
        choices=Category.choices,
        default=Category.OTHER,
        verbose_name='Категорія'
    )

    device_type = models.CharField(
        max_length=20,
        choices=DeviceType.choices,
        default=DeviceType.PC,
        verbose_name='Тип пристрою'
    )

    resolution = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='Роздільна здатність'
    )

    description = models.TextField(
        blank=True,
        verbose_name='Опис'
    )

    downloads = models.PositiveIntegerField(
        default=0,
        verbose_name='Кількість завантажень'
    )

    is_featured = models.BooleanField(
        default=False,
        verbose_name='Рекомендовані'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата створення'
    )

    class Meta:
        verbose_name = 'Шпалери'
        verbose_name_plural = 'Шпалери'
        ordering = ['-created_at']

    def __str__(self):
        return self.title
