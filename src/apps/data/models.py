from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify


class Analysis(models.Model):
    title = models.CharField(_('title'), max_length=50)
    slug = models.SlugField(max_length=60)
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Analysis")
        verbose_name_plural = _("Analyses")
        ordering = ['title', 'timestamp']

    def save(self):
        self.slug = slugify(self.title)
        super().save()

    def __str__(self):
        return self.title


class Word(models.Model):
    word = models.TextField(_('word'))
    frequency = models.PositiveIntegerField(_('frequency'), default=0)
    analisis = models.ForeignKey('data.Analysis', on_delete=models.CASCADE,
                                 related_name='words')

    class Meta:
        verbose_name = _("Word")
        verbose_name_plural = _("Words")

    def __str__(self):
        return self.name


class AudienciasQuestion(models.Model):
    room_id = models.PositiveIntegerField(_('room id'), default=0)
    question_id = models.PositiveIntegerField(_('question id'), default=0)
    question = models.TextField(_('question'))

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")

    def __str__(self):
        return self.question
