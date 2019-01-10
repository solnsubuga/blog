from django.test import TestCase, Client
from autofixture import AutoFixture
from django.contrib.auth.models import User
from articles.models import Article, Category


class BaseTestCase(TestCase):
    def setUp(self):
        self.category = AutoFixture(Category).create(1)[0]
        self.writer = User.objects.get_or_create(
            username='test', email='test@test.com', password='test')[0]
        self.articles = AutoFixture(Article, field_values={
            'writer': self.writer, 'category': self.category, 'status': 'published'}).create(2)

        self.client = Client()
