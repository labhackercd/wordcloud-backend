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
    rooms_id = [
        '1538', '1537', '1533', '1531', '1530', '1529', '1528', '1527', '1526', '1525',
        '1523', '1520', '1519', '1518', '1517', '1516', '1515', '1514', '1513', '1512'
    ]

    for id in rooms_id:
        url = settings.AUDIENCIAS_API_URL + 'question/?room__id=%s' % str(id)
        request = get_json_request(url)
        data += request['results']

        while request['next']:
            page += 1
            data += get_json_request(url, page)

    create_questions(data)

    return _('Questions was fetched successfully.')
