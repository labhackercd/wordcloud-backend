FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache tzdata && \
    cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime && \
    echo "America/Sao_Paulo" > /etc/timezone

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN apk add --no-cache bash

RUN mkdir -p /var/labhacker/wordcloud_backend

WORKDIR /var/labhacker/wordcloud_backend
COPY requirements.txt /var/labhacker/wordcloud_backend/
RUN pip install -r requirements.txt
COPY . /var/labhacker/wordcloud_backend/

RUN chmod 755 start_web.sh
RUN chmod 755 start_celery_beat.sh

CMD ["python3", "src/manage.py", "runserver", "0.0.0.0:8000"]
