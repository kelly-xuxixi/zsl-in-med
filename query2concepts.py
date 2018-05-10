import math
import operator
from util import get_words_from_sentences
from config import cfg
from nltk.corpus import wordnet as wn
import spacy
import numpy as np


def get_concepts(query):
    word_list = get_words_from_sentences(query)
    key_words_and_probs = get_key_words(word_list)
    key_words = [item[0] for item in key_words_and_probs]
    print(key_words_and_probs)
    print(key_words)
    concepts = get_related_concepts(key_words)
    # return concepts
    return []


def process_synonyms(word_list):
    print('processing synonyms')
    syn_dict = {}
    for word in word_list:
        syns = wn.synsets(word)
        str_syns = []
        for syn in syns:
            str_syns.append(str(syn)[8:-7])
        syn_dict[word] = str_syns
    print(syn_dict)
    for i in range(len(word_list)):
        for j in range(len(word_list)):
            x = word_list[i]
            y = word_list[j]
            if x == y:
                continue
            if x in syn_dict[y] or y in syn_dict[x]:
                print(x, y)
                word_list[j] = x
    return word_list


def get_key_words(word_list):
    word_list = process_synonyms(word_list)
    stat = {}
    print('calculating tf-idf')
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
    return sorted_words[:10]
    # return [item[0] for item in sorted_words[:5]]


def get_related_concepts(key_words):
    file = open('concepts.txt', 'r')
    lines = file.read()
    concepts = []
    tokens = []
    nlp = spacy.load('en_core_web_md')
    for line in lines:
        line = line.strip().strip(',')
        print(line)
        concepts.append(line)
        tokens.append(nlp(u'%s' % line))
    # tokens = map(lambda t: nlp(u'%s' % t), concepts)
    key_concept_similarity = []
    for key in key_words:
        sim = []
        key_token = nlp(u'%s' % key)
        for token in tokens:
            sim.append(token.similarity(key_token))
        most_sim = np.argsort(sim)[::-1]
        print(key, tokens[most_sim][:5])
        key_concept_similarity.append(sim)
    return key_concept_similarity

    # concepts = []
    # for concept in concepts:

    return concepts


def compute_idf(word):
    file = open('corpus_words.txt', 'r')
    content = file.read()
    corpus_length = int(content.split('\n')[0])
    word_list = content.split('\n')[1].split(' ')
    # print(word, word_list.count(word))
    return math.log(float(corpus_length) / (word_list.count(word) + 1))

