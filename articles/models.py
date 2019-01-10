from django.db import models
from django.conf import settings
from django.urls import reverse


class TimeStampedModel(models.Model):
    """Abstract model with timestamps

    Inherit from this model to have timestamps added to child model
    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStampedModel):
    """Category model
    """
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Article(TimeStampedModel):
    """Article model
    """

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    writer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=125)
    # add slug to build clean urls
    slug = models.SlugField(max_length=250, unique_for_date='created')
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default='draft')
    image = models.ImageField(upload_to='articles',
                              blank=True)

    class Meta:
        ordering = ('-created', )

    def get_url(self):
        """Absolute url for article """
        return reverse('articles:article_detail',
                       args=[self.id, self.slug])

    def __str__(self):
        return self.title
