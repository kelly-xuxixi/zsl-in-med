import os
from itertools import chain
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import numpy as np


def get_words_from_sentences(query):
    query = query.lower()
    words = word_tokenize(query)
    words = list(filter(lambda t: (t != '.' and t != ',' and t != ':'), words))
    words = list(filter(lambda t: t not in stopwords.words('english'), words))
    words = list(map(lambda t: t.split('/'), words))
    words = list(chain(*words))
    return words


def get_word_list_from_corpus():
    # write all words in the corpus into one file
    # (unique words in each query)
    corpus_path = 'metadata'
    files = os.listdir(corpus_path)
    corpus_list = []
    for file in files:
        print(file)
        corpus_list.append(open(os.path.join(corpus_path, file), 'r').read())
    corpus_word_list = list(map(set, map(get_words_from_sentences, corpus_list)))
    word_list = list(chain(*corpus_word_list))
    print(word_list)
    file = open('corpus_words.txt', 'w')
    file.write(str(len(corpus_list)) + '\n')
    for word in word_list:
        file.write(word + ' ')
    file.close()


# returns the top1 string
def print_prob(prob, file_path):
    synset = [l.strip() for l in open(file_path).readlines()]

    # print prob
    pred = np.argsort(prob)[::-1]

    # Get top1 label
    top1 = synset[pred[0]]
    print(("Top1: ", top1, prob[pred[0]]))
    # Get top5 label
    top5 = [(synset[pred[i]], prob[pred[i]]) for i in range(5)]
    print(("Top5: ", top5))
    return top1


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

