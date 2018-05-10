import sys
import math
import numpy as np

from query2concepts import get_concepts
from util import get_words_from_sentences
from util import get_word_list_from_corpus
from config import cfg
import os
from nltk.corpus import wordnet as wn



def run():
    query_path = os.path.join('metadata', 'E022.txt')
    file = open(query_path, 'r')
    query_info = file.read()
    # query_info = 'Bee keeping. One or more people perform activities associated with the keeping of honeybees. ' \
    #              'Bee keeping refers to the maintenance of honeybees by humans. ' \
    #              'A beekeeper keeps bees in order to collect products of the hive ' \
    #              'to pollinate crops, or to produce bees for sale to others. ' \
    #              'bee, bee keeper, smoke, honey, knife.'
    concepts = get_concepts(query_info)
    # concept_rankings = rankings[concepts, :]


def main():
    # get_word_list_from_corpus()
    # print(compute_idf('definition'))
    run()


if __name__ == '__main__':
    main()
