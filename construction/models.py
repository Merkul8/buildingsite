from django.db import models
from django.urls import reverse


class ConstructionModel(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    content = models.TextField(blank=True, verbose_name='Содержание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    photo_2 = models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото-2')
    photo_3 = models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото-3')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    price = models.CharField(blank=True, max_length=150, verbose_name='Цена')
    category = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.PROTECT, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('home', kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Вид работ'
        verbose_name_plural = 'Виды работ'
        ordering = ['created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Категория')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

