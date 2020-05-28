FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN mkdir -p /var/labhacker/wordcloud_backend

WORKDIR /var/labhacker/wordcloud_backend
COPY requirements.txt /var/labhacker/wordcloud_backend/
RUN pip install -r requirements.txt
COPY . /var/labhacker/wordcloud_backend/