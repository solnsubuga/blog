from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.conf import settings

from .models import Article


class ArticleListView(View):
    """ Articles list view
    """

    def get(self, request):
        category_name = request.GET.get('category')
        q = Q(status='published',
              category__name=category_name) if category_name else Q(
            status='published')

        articles = Article.objects.filter(q).all()

        paginator = Paginator(articles, settings.PAGINATION_AMOUNT)
        page = request.GET.get('page')
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            articles = paginator.page(1)
        except EmptyPage:
            articles = paginator.page(paginator.num_pages)

        return render(request, 'list.html', {
            'page': page, 'articles': articles,
            'category': category_name
        })
