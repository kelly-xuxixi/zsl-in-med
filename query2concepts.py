import math
import operator
from util import get_words_from_sentences
from config import cfg
from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic
import spacy
import numpy as np


def get_key_and_concepts(query):
    # split words from query using nltk.tokenizer
    word_list = get_words_from_sentences(query)
    # get key words and their importance
    key_words_and_probs = get_key_words(word_list)
    key_words = [item[0] for item in key_words_and_probs]
    key_words_importance = [item[1] for item in key_words_and_probs]
    print(len(key_words), key_words_and_probs)
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
    # return sorted_words[:10]
    key_words = filter_keywords(sorted_words)
    return key_words


def get_related_concepts_with_word2vec(key_words):
    file = open('concepts.txt', 'r')
    lines = file.readlines()
    concept_tokens = []
    nlp = spacy.load('en_core_web_md')
    # transfer concepts to word2vec tokens
    for line in lines:
        line = line.strip().strip(',')
        line = line.replace('_', ' ')
        line = line.replace('/', ' ')
        concept_tokens.append(nlp(u'%s' % line))
    # compute key_concept matrix
    key_concept_similarity = []
    for key in key_words:
        sim = []
        key_token = nlp(u'%s' % key)
        for token in concept_tokens:
            if cfg.use_square_in_concept_selection:
                sim.append(np.square(token.similarity(key_token)))
            else:
                sim.append(token.similarity(key_token))
        most_sim = np.argsort(sim)[::-1]
        print(key, ' most sim: ', [(concept_tokens[most_sim[i]], sim[most_sim[i]]) for i in range(5)])
        key_concept_similarity.append(sim)
    return key_concept_similarity


def get_related_concepts_with_wordnet(key_words):
    brown_ic = wordnet_ic.ic('ic-brown.dat')
    file = open('imagenet_1000.txt', 'r')
    lines = file.readlines()
    concept_synsets = []
    # transfer concepts to wordnet synsets
    for line in lines:
        id = line.split(' ')[0][1:]
        if id[0] == '0':
            id = id[1:]
        concept_synsets.append(get_synset_from_id(id))
    file = open('places365.txt')
    lines = file.readlines()
    for line in lines:
        concept_synsets.append(get_synset_from_word(line.strip()))
    # compute key_concept matrix
    key_concept_similarity = []
    for key in key_words:
        sim = []
        key_synset = get_synset_from_word(key)
        for synset in concept_synsets:
            try:
                sim.append(synset.res_similarity(key_synset, brown_ic))
            except:
                sim.append(0.0)
        most_sim = np.argsort(sim)[::-1]
        print(key, ' most sim: ', [(concept_synsets[most_sim[i]], sim[most_sim[i]]) for i in range(5)])
        key_concept_similarity.append(sim)
    return key_concept_similarity


def get_synset_from_word(word):
    synsets = wn.synsets(word)
    if len(synsets) > 0:
        return synsets[0]
    else:
        print(word + ' has no synsets')
        return wn.synsets('nothing')[0]


def get_synset_from_id(id):
    try:
        synset = wn._synset_from_pos_and_offset('n', int(id))
        return synset
    except:
        print(id)
        return wn.synsets('nothing')[0]


def process_synonyms(word_list):
    # print('processing synonyms')
    # get synonyms for each word
    syn_dict = {}
    for word in word_list:
        syns = wn.synsets(word)
        str_syns = []
        for syn in syns:
            str_syns.append(str(syn)[8:-7])
        syn_dict[word] = str_syns
    # print(syn_dict)
    # replace words with their synonyms
    for i in range(len(word_list)):
        for j in range(len(word_list)):
            x = word_list[i]
            y = word_list[j]
            if x == y:
                continue
            if x in syn_dict[y] or y in syn_dict[x]:
                # print(x, y)
                word_list[j] = x
    return word_list


def filter_keywords(sorted_words):
    key_words = {}
    cfg.delete_not_nones = False
    cfg.delete_ambivalent_words = True
    cfg.set_threshold = True
    cfg.threshold = 2.3
    for word in sorted_words.keys():
        flag = True
        if cfg.delete_not_nones and wn.synsets(word)[0].pos() != 'n':
            flag = False
        if cfg.delete_ambivalent_words and len(wn.synsets(word)) > 10:
            flag = False
        if cfg.set_threshold and sorted_words[word] < cfg.threshold:
            flag = False
        if flag:
            key_words[word] = sorted_words[word]
    return key_words


def compute_idf(word):
    file = open('corpus_words.txt', 'r')
    content = file.read()
    corpus_length = int(content.split('\n')[0])
    word_list = content.split('\n')[1].split(' ')
    return math.log(float(corpus_length) / (word_list.count(word) + 1))
