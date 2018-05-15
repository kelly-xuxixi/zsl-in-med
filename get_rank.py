import numpy as np


def get_rank():
    key_importance = np.loadtxt('key_importance.txt')
    key_concept_similarity = np.loadtxt('key_concept_similarity.txt')
    probs = np.loadtxt('mean_probs.txt')
    print(key_importance.shape, key_concept_similarity.shape, probs.shape)
    key_importance.shape = (10, 1)
    key_importance = np.transpose(key_importance)
    probs = np.transpose(probs)
    print(key_importance.shape, key_concept_similarity.shape, probs.shape)
    result = np.dot(key_importance, key_concept_similarity)
    result = np.dot(result, probs)
    print(result.shape)
    result = np.argsort(result[0])[::-1]
    print(result[:10])


if __name__ == '__main__':
    get_rank()