# Generated by Django 4.1.7 on 2023-03-19 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construction', '0006_alter_constructionmodel_options_construction'),
    ]

    operations = [
        migrations.AddField(
            model_name='construction',
            name='floors',
            field=models.CharField(blank=True, max_length=150, verbose_name='Кол-во этажей'),
        ),
        migrations.AddField(
            model_name='construction',
            name='size',
            field=models.CharField(blank=True, max_length=150, verbose_name='Размер помещения'),
        ),
        migrations.DeleteModel(
            name='ConstructionModel',
        ),
    ]