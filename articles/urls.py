from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import ArticleListView, ArticleDetailView

app_name = 'articles'

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/<slug>/', ArticleDetailView.as_view(), name='article_detail')
]

# Bad idea don't do this in production
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
