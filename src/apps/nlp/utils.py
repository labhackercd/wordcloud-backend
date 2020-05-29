from apps.nlp.stopwords import EXTRA_STOPWORDS
from nltk import word_tokenize
from nltk.util import ngrams
from nltk.corpus import stopwords as nltk_stopwords
from collections import Counter
from string import punctuation


def get_tokens(questions, extra_stopwords=None):
    """
    Funçao que retorna tokens de discursos removendo as "stopwords".
    Argumentos:
        speeches: Recebe uma lista de discursos.
        stopwords: Recebe uma lista de palavras a serem retiradas dos textos.
    Retorna:
        Uma lista palavras do discurso que nao estão nas "stopwords".
    """
    stopwords = nltk_stopwords.words(
        'portuguese') + list(punctuation) + EXTRA_STOPWORDS
    stopwords = [word for word in stopwords]
    if extra_stopwords:
        stopwords += extra_stopwords
    tokens = []
    for text in questions:
        tokens += [i for i in word_tokenize(text.lower(),
                                            language='portuguese') if i not in stopwords]

    return tokens


def ngrams_by_limit(tokens, n, limit):
    """
    Função que retorna uma lista de ngrams de acordo com os argumento passados.
    Argumentos:
        tokens: Recebe uma lista de tokens ja processados pelo nltk.word_tokenize.
        n: Recebe o número de palavras que deseja dividir o ngram.
        limit: Recebe o limite mínimo de ocorrência.
    Retorna:
        Uma lista de ngrams com ocorrência maior que "limite" e com "n" palavras.
    """
    ngrams_count = Counter(ngrams(tokens, n)).most_common()
    result = [x for x in ngrams_count if x[1] >= limit]
    return result


def clean_tokens(tokens, bigrams=[], extra_stopwords=None):
    """
    Função que retorna uma lista de tokens filtradas pelos argumentos passados.
    Argumentos:
        tokens: Recebe uma lista de tokens já processados pelo nltk.word_tokenize.
        trigrams: Recebe uma lista de trigramas.
        bigrams: Recebe uma lista de bigramas.
        extra_stopwords: Recebe uma lista de stopwords.
    Retorna:
        Uma lista de tokens removendo os n-gramas e stopwords passados nos argumentos.
    """

    if bigrams:
        pos_bigram = []
        for i in range(len(tokens)-1):
            for word1, word2 in bigrams:
                if tokens[i] == word1 and tokens[i+1] == word2:
                    pos_bigram.append(i)

        for pos in reversed(pos_bigram):
            del tokens[pos:pos+2]

    if extra_stopwords:
        new_tokens = [
            token for token in tokens if token not in extra_stopwords]
    else:
        new_tokens = tokens

    return new_tokens
