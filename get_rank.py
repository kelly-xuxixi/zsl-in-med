import numpy as np
import util


def get_rank():
    key_importance = np.loadtxt('key_importance.txt')
    key_concept_similarity = np.loadtxt('key_concept_similarity.txt')
    probs = np.loadtxt('mean_probs.txt')
    print(key_importance.shape, key_concept_similarity.shape, probs.shape)
    key_importance.shape = (10, 1)
    key_importance = np.transpose(key_importance)
    tran_probs = np.transpose(probs)
    print(key_importance.shape, key_concept_similarity.shape, tran_probs.shape)
    result = np.dot(key_importance, key_concept_similarity)
    result = np.dot(result, tran_probs)
    print(result.shape)
    result = np.argsort(result[0])[::-1]
    print(result[:10])
    video_name = open('event_video_list.txt', 'r').readlines()
    for id in result[:10]:
        print(video_name[id])
        util.print_prob(probs[id], './synset.txt')


if __name__ == '__main__':
    get_rank()