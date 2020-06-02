from apps.nlp.utils import get_tokens, ngrams_by_limit, clean_tokens
from apps.nlp.stopwords import ONEGRAM_STOPWORDS
from apps.data.models import AudienciasQuestion
from collections import Counter
from django.http import JsonResponse


def multigrams_analysis(request):
    questions = AudienciasQuestion.objects.values_list('question', flat=True)
    tokens = get_tokens(questions)

    # Determinamos o limite de ocorrências usado no algoritmo
    limit = Counter(tokens).most_common(int(len(questions) * 0.2))[-1][1]
    if limit < 3:
        limit = 3

    # Obtendo termos com 2 palavras
    bigrams = ngrams_by_limit(tokens, 2, limit)

    # Obtendo termos com 1 palavras
    stop_bigrams = []

    if bigrams:
        stop_bigrams = list(list(zip(*bigrams))[0])

    onegram_tokens = clean_tokens(tokens, stop_bigrams,
                                  ONEGRAM_STOPWORDS)
    onegrams = ngrams_by_limit(onegram_tokens, 1, limit)

    result_tokens = onegrams + bigrams
    result_tokens.sort(key=lambda x: x[1], reverse=True)

    return JsonResponse(result_tokens, safe=False)
