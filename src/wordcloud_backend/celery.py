import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wordcloud_backend.settings')

app = Celery('wordcloud_backend')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))