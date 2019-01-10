from django.contrib.auth.models import User
from django.shortcuts import reverse
from autofixture import AutoFixture
from articles.models import Category, Article

from .base import BaseTestCase


class ViewArticlesTestCase(BaseTestCase):
    def test_it_renders_published_posts(self):
        """Should render published articles
        """
        res = self.client.get(reverse('articles:article_list'))
        article = self.articles[0]
        self.assertContains(res, article.title)

    def test_renders_categorised_posts(self):
        """Should render articles in a given category
        """
        url = '{0}?category={1}'.format(
            reverse('articles:article_list'), self.category.name)
        res = self.client.get(url)
        self.assertContains(res, self.category.name)

    def test_should_handle_pagination_for_empty_page(self):
        """Should gracefully render paginated articles when page requested is empty
        """
        url = '{0}?page={1}'.format(
            reverse('articles:article_list'), 100)
        res = self.client.get(url)
        self.assertContains(res, self.articles[0].title)

    def test_view_article(self):
        """ Should render a single article"""
        article = self.articles[0]
        url = article.get_url()
        res = self.client.get(url)
        self.assertContains(res, article.title)
