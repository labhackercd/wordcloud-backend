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
    created_questions = 0
    questions_exists = AudienciasQuestion.objects.all().values_list(
        'question_id', flat=True)
    for question in data:
        if question['id'] not in questions_exists:
            AudienciasQuestion.objects.create(
                room_id=question['room'],
                question_id=question['id'],
                question=question['question']
            )
            created_questions += 1

    return created_questions


@celery_app.task
def get_questions():
    data = []

    response = requests.get(settings.AUDIENCIAS_API_URL).json()
    data = response['results']

    while response['next']:
        response = requests.get(response['next']).json()
        data += response['results']

    created_questions = create_questions(data)

    return _('%s questions was fetched successfully.' % str(created_questions))
