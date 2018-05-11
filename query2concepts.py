import math
import operator
from util import get_words_from_sentences
from config import cfg
from nltk.corpus import wordnet as wn
import spacy
import numpy as np


def get_key_and_concepts(query):
    # split words from query using nltk.tokenizer
    word_list = get_words_from_sentences(query)
    # get key words and their importance
    key_words_and_probs = get_key_words(word_list)
    key_words = [item[0] for item in key_words_and_probs]
    key_words_importance = [item[1] for item in key_words_and_probs]
    print(key_words_and_probs)
    print(key_words)
    # get similarity matrix between key and concepts
    if cfg.use_word2vec:
        key_concept_sim = get_related_concepts_with_word2vec(key_words)
    else:
        key_concept_sim = get_related_concepts_with_wordnet(key_words)
    return key_words_importance, key_concept_sim


def get_key_words(word_list):
    # unify synonyms
    if cfg.unify_synonyms:
        word_list = process_synonyms(word_list)
    # calculate word frequency in current query
    word_importance = {}
    for word in word_list:
        try:
            word_importance[word] += 1
        except KeyError:
            word_importance[word] = 1
    # calculate word distinctiveness in corpus
    if cfg.use_tfidf:
        for word in word_importance.keys():
            word_importance[word] *= compute_idf(word)
            if cfg.use_log_in_word_importance:
                word_importance[word] = math.log(word_importance[word] + 1)
    # sort word in accordance to word importance
    sorted_words = sorted(word_importance.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_words[:10]


def get_related_concepts_with_word2vec(key_words):
    file = open('concepts.txt', 'r')
    lines = file.readlines()
    concept_tokens = []
    nlp = spacy.load('en_core_web_md')
    # transfer concepts to word2vec tokens
    for line in lines:
        line = line.strip().strip(',')
        line = line.replace('_', ' ')
        concept_tokens.append(nlp(u'%s' % line))
    # compute key_concept matrix
    key_concept_similarity = []
    for key in key_words:
        sim = []
        key_token = nlp(u'%s' % key)
        for token in concept_tokens:
            if cfg.use_log_in_concept_selection:
                sim.append(token.similarity(key_token)) # how to maximize larger ones and minimize smaller ones?
            else:
                if token.similarity(key_token) == 0:
                    print(token, ' has no vector')
                sim.append(token.similarity(key_token))
        most_sim = np.argsort(sim)[::-1]
        print(key, ' most sim: ', [(concept_tokens[most_sim[i]], sim[most_sim[i]]) for i in range(5)])
        key_concept_similarity.append(sim)
    return key_concept_similarity


def get_related_concepts_with_wordnet(key_words):
    return []


def process_synonyms(word_list):
    print('processing synonyms')
    # get synonyms for each word
    syn_dict = {}
    for word in word_list:
        syns = wn.synsets(word)
        str_syns = []
        for syn in syns:
            str_syns.append(str(syn)[8:-7])
        syn_dict[word] = str_syns
    print(syn_dict)
    # replace words with their synonyms
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


def compute_idf(word):
    file = open('corpus_words.txt', 'r')
    content = file.read()
    corpus_length = int(content.split('\n')[0])
    word_list = content.split('\n')[1].split(' ')
    return math.log(float(corpus_length) / (word_list.count(word) + 1))
