from django.contrib import admin
from .models import Category, Article


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('name', 'created', )


@admin.register(Article)
class AdminArticle(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category',
                    'image', 'writer', 'status', 'created', )
    search_fields = ('title', )
    prepopulated_fields = {'slug': ('title', )}
