from query2concepts import get_key_and_concepts
import os
import numpy as np


def get_matrix_from_query():
    query_path = os.path.join('metadata', 'E022.txt')
    file = open(query_path, 'r')
    query_info = file.read()
    key_importance, key_concept_similarity = get_key_and_concepts(query_info)
    key_importance = np.array(key_importance)
    key_concept_similarity = np.array(key_concept_similarity)
    np.savetxt('key_importance.txt', key_importance)
    np.savetxt('key_concept_similarity.txt', key_concept_similarity)


def main():
    # get_word_list_from_corpus()
    # print(compute_idf('definition'))
    get_matrix_from_query()


if __name__ == '__main__':
    main()
