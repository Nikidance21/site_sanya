from django.urls import path

from django.conf import settings
from django.views.decorators.cache import never_cache
from django.views.static import serve
from django.urls import path
from .views import index

urlpatterns = [
]
if settings.DEBUG:
    urlpatterns.append(path('static/<path:path>', never_cache(serve)))


app_name = 'main'

urlpatterns = [
   path('', index, name='index')
]

