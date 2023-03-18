from django.contrib import admin

from .models import ConstructionModel, Category, Construction


class ConstructionModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'created_at')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')


class ConstructionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'price')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_filter = ('category',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title', )


admin.site.register(ConstructionModel, ConstructionModelAdmin)
admin.site.register(Category, CategoryAdmin )
admin.site.register(Construction, ConstructionAdmin)
