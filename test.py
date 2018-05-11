from query2concepts import get_key_and_concepts
import os


def get_matrix_from_query():
    query_path = os.path.join('metadata', 'E022.txt')
    file = open(query_path, 'r')
    query_info = file.read()
    key_importance, key_concept_similarity = get_key_and_concepts(query_info)
    # print('key_importance: \n', key_importance)
    # print('key_concept_similarity: \n', key_concept_similarity)
    # concept_rankings = rankings[concepts, :]


def main():
    # get_word_list_from_corpus()
    # print(compute_idf('definition'))
    get_matrix_from_query()


if __name__ == '__main__':
    main()
