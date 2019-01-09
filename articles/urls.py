from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


app_name = 'articles'

urlpatterns = [

]

# Bad idea don't do this in production
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
