import numpy as np


def get_rank():
    key_importance = np.loadtxt('key_importance.txt')
    key_concept_similarity = np.loadtxt('key_concept_similarity.txt')
    probs = np.loadtxt('mean_probs.txt')
    print(key_importance.shape, key_concept_similarity.shape, probs.shape)


if __name__ == '__main__':
    get_rank()