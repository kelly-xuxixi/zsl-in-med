import sys
import math

from query2concepts import get_concepts
from util import get_words_from_sentences
from util import get_word_list_from_corpus
from config import cfg


def run():
    query_path = ''
    query_info = 'Bee keeping. One or more people perform activities associated with the keeping of honeybees. ' \
                 'Bee keeping refers to the maintenance of honeybees by humans. ' \
                 'A beekeeper keeps bees in order to collect products of the hive ' \
                 'to pollinate crops, or to produce bees for sale to others. ' \
                 'bee, bee keeper, smoke, honey, knife.'
    concepts = get_concepts(query_info)
    # concept_rankings = rankings[concepts, :]


def compute_idf(word):
    file = open('corpus_words.txt', 'r')
    content = file.read()
    corpus_length = int(content.split('\n')[0])
    word_list = content.split('\n')[1].split(' ')
    print(corpus_length)
    print(word_list)
    return math.log(corpus_length / (word_list.count(word) + 1))


def main():
    # get_word_list_from_corpus()
    # print(compute_idf('zz'))
    run()

if __name__ == '__main__':
    main()
