"""blog URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'Blog Admin Center'
admin.site.site_title = 'Blog'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('articles.urls', namespace='articles')),
]
