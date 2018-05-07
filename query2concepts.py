import math
import operator
from util import get_words_from_sentences
from config import cfg


def get_concepts(query):
    word_list = get_words_from_sentences(query)
    key_words = get_key_words(word_list)
    print(key_words)
    concepts = get_related_concepts(key_words)
    # return concepts
    return []


def get_key_words(word_list):
    stat = {}
    for word in word_list:
        try:
            stat[word] += 1
        except KeyError:
            stat[word] = 1
    if cfg.use_tfidf:
        for word in stat.keys():
            stat[word] *= compute_idf(word)
    sorted_words = sorted(stat.items(), key=operator.itemgetter(1), reverse=True)
    print(sorted_words)
    return [item[0] for item in sorted_words[:5]]


def get_related_concepts(key_words):
    concepts = []
    # for concept in concepts:

    return concepts


def compute_idf(word):
    file = open('corpus_words.txt', 'r')
    content = file.read()
    corpus_length = int(content.split('\n')[0])
    word_list = content.split('\n')[1].split(' ')
    print(corpus_length)
    print(word_list)
    return math.log(corpus_length / (word_list.count(word) + 1))

