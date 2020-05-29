from django.contrib import admin
from django.urls import path
from apps.nlp.views import multigrams_analysis

urlpatterns = [
    path('', multigrams_analysis),
    path('admin/', admin.site.urls),
]
