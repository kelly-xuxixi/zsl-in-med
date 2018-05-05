import sys
from query2concepts import get_concepts
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


def main():
    run()

if __name__ == '__main__':
    main()
