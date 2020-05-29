from django.contrib import admin

from .models import Analysis, Word, AudienciasQuestion


@admin.register(Analysis)
class AnalysisAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ('slug',)


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('id', 'word', 'frequency', 'analisis')
    list_filter = ('analisis',)


@admin.register(AudienciasQuestion)
class AudienciasQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'room_id', 'question_id', 'question')
