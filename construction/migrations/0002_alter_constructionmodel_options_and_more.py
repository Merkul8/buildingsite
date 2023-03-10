# Generated by Django 4.1.7 on 2023-02-23 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construction', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='constructionmodel',
            options={'verbose_name': 'Вид работ', 'verbose_name_plural': 'Виды работ'},
        ),
        migrations.AlterField(
            model_name='constructionmodel',
            name='content',
            field=models.TextField(blank=True, verbose_name='Содержание'),
        ),
        migrations.AlterField(
            model_name='constructionmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='constructionmodel',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='constructionmodel',
            name='photo',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='constructionmodel',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Название'),
        ),
    ]
