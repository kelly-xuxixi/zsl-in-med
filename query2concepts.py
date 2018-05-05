from util import get_words_from_sentences


def get_key_words(word_list):
    stat = {}
    for word in word_list:
        stat[word] += 1
    sorted(stat)
    print(stat)
    return stat.keys()


def get_related_concepts(key_words):
    concepts = []
    return concepts


def get_concepts(query):
    word_list = get_words_from_sentences(query)
    # key_words = get_key_words(word_list)
    # concepts = get_related_concepts(key_words)
    # return concepts
    return []
