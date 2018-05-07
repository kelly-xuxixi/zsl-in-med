import numpy as np
import math
import sys
from itertools import chain
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def get_words_from_sentences(query):
    query = query.lower()
    words = word_tokenize(query)
    words = list(filter(lambda t: (t != '.' and t != ','), words))
    words = list(filter(lambda t: t not in stopwords.words('english'), words))
    # print(words)
    return words


def get_word_list_from_corpus():
    corpus_path = ''
    corpus_list = []
    # for file in corpus_path:
    #     corpus_list.append(open(file, 'r').read())
    corpus_list.append('aa aa bb cc dd ee')
    corpus_list.append('aa bb cc ff gg')
    corpus_list.append('aa dd hh')
    corpus_word_list = list(map(set, map(get_words_from_sentences, corpus_list)))
    word_list = list(chain(*corpus_word_list))
    print(word_list)
    file = open('corpus_words.txt', 'w')
    file.write(str(len(corpus_list)) + '\n')
    for word in word_list:
        file.write(word + ' ')
    file.close()


# based on https://stackoverflow.com/questions/2352181/how-to-use-a-dot-to-access-members-of-dictionary
class Dict(dict):
    """
    Example:
    m = Dict({'first_name': 'Eduardo'}, last_name='Pool', age=24, sports=['Soccer'])
    """

    def __init__(self, *args, **kwargs):
        super(Dict, self).__init__(*args, **kwargs)
        for arg in args:
            if isinstance(arg, dict):
                for k, v in arg.items():
                    self[k] = v

        if kwargs:
            for k, v in kwargs.items():
                self[k] = v

    def __getattr__(self, attr):
        return self[attr]

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __setitem__(self, key, value):
        super(Dict, self).__setitem__(key, value)
        self.__dict__.update({key: value})

    def __delattr__(self, item):
        self.__delitem__(item)

    def __delitem__(self, key):
        super(Dict, self).__delitem__(key)
        del self.__dict__[key]

