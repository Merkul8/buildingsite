# Generated by Django 4.1.7 on 2023-03-09 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construction', '0004_alter_constructionmodel_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='constructionmodel',
            name='photo_2',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото-2'),
        ),
        migrations.AddField(
            model_name='constructionmodel',
            name='photo_3',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото-3'),
        ),
        migrations.AddField(
            model_name='constructionmodel',
            name='price',
            field=models.CharField(blank=True, max_length=150, verbose_name='Цена'),
        ),
    ]
