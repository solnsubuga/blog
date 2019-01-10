from django.urls import path
from django.conf.urls.static import static

from .views import ArticleListView, ArticleDetailView

app_name = 'articles'

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/<slug>/', ArticleDetailView.as_view(), name='article_detail')
]
