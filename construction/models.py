from django.db import models
from django.urls import reverse


class Construction(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    slug = models.SlugField(unique=True, blank=True, verbose_name='Url')
    content = models.TextField(blank=True, verbose_name='Содержание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    photo_2 = models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото-2')
    photo_3 = models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото-3')
    price = models.CharField(blank=True, max_length=150, verbose_name='Цена')
    category = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.PROTECT, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('category_item', kwargs={'slug': self.slug})
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Вид работ'
        verbose_name_plural = 'Виды работ'

        
class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Категория')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

