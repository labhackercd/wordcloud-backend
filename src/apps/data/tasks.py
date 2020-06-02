from django.utils.translation import ugettext_lazy as _
from apps.data.models import AudienciasQuestion
from wordcloud_backend import celery_app
from celery.utils.log import get_task_logger
from django.conf import settings
import requests

logger = get_task_logger(__name__)


def get_json_request(url, page=1):
    return requests.get(url + '&page=%s' % page).json()


def create_questions(data):
    for question in data:
        AudienciasQuestion.objects.create(
            room_id=question['room'],
            question_id=question['id'],
            question=question['question']
        )


@celery_app.task
def get_questions():
    data = []

    response = requests.get(settings.AUDIENCIAS_API_URL).json()
    data = response['results']

    while response['next']:
        response = requests.get(response['next']).json()
        data += response['results']

    create_questions(data)

    return _('Questions was fetched successfully.')
