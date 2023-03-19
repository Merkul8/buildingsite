from django.contrib import admin

from .models import Category, Construction


class ConstructionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'price')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_filter = ('category',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title', )


admin.site.register(Category, CategoryAdmin )
admin.site.register(Construction, ConstructionAdmin)
