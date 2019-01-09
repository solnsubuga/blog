from unittest import TestCase
from django.contrib.auth.models import User
from autofixture import AutoFixture
from articles.models import Category, Article


class ModelsTestCase(TestCase):
    def setUp(self):
        self.category = AutoFixture(Category).create(1)[0]
        self.writer = User.objects.get_or_create(
            username='test', email='test@test.com', password='test')[0]
        self.article = AutoFixture(Article, field_values={
                                   'writer': self.writer, 'category': self.category}).create(1)[0]

    def test_category_creation(self):
        """Should test a category is created
        """
        self.assertTrue(isinstance(self.category, Category))
        self.assertEqual(self.category.__str__(), self.category.name)

    def test_article_creation(self):
        """Should test an article is created
        """
        self.assertTrue(isinstance(self.article, Article))
        self.assertEqual(self.article.__str__(), self.article.title)
