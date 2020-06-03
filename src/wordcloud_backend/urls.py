from django.contrib import admin
from django.urls import path
from apps.nlp.views import multigrams_analysis
from django.conf import settings

if settings.URL_PREFIX:
    prefix = '%s/' % (settings.URL_PREFIX)
else:
    prefix = ''

urlpatterns = [
    path(prefix + '', multigrams_analysis),
    path(prefix + 'admin/', admin.site.urls),
]

admin.site.site_header = 'Wordcloud Backend'
