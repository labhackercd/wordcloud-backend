from django.contrib import admin
from django.urls import path
from apps.nlp.views import multigrams_analysis
from django.conf import settings

if settings.URL_PREFIX:
    prefix = r'^%s/' % (settings.URL_PREFIX)
else:
    prefix = r'^'

urlpatterns = [
    path(prefix + r'', multigrams_analysis),
    path(prefix + r'admin/', admin.site.urls),
]

admin.site.site_header = 'Wordcloud Backend'
