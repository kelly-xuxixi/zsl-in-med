import numpy as np
import util
import os


def get_rank(importance_path, similarity_path):
    print(importance_path, similarity_path)
    key_importance = np.loadtxt(importance_path)
    key_concept_similarity = np.loadtxt(similarity_path)
    key_importance.shape = (10, 1)
    key_importance = np.transpose(key_importance)
    tran_probs = np.transpose(probs)
    result = np.dot(key_importance, key_concept_similarity)
    result = np.dot(result, tran_probs)
    result = result[0]
    top_ids = np.argsort(result)[::-1]
    print(top_ids[:10])
    video_name = open('event_video_list.txt', 'r').readlines()
    for id in top_ids[:10]:
        print(video_name[id].strip())
        util.print_prob(probs[id], './synset.txt')
    print('\n')
    return result


if __name__ == '__main__':
    stats_root = './stats'
    files = os.listdir(stats_root)
    files.sort()
    all_ranks = []
    probs = np.loadtxt('mean_probs.txt')
    for i in range(20):
        assert files[i*2].endswith('similarity.txt') and files[i*2+1].endswith('importance.txt')
        rank = get_rank(os.path.join(stats_root, files[i*2+1]), os.path.join(stats_root, files[i*2]))
        all_ranks.append(rank)
    all_ranks = np.vstack(all_ranks)
    print(all_ranks.shape)
    np.savetxt('all_ranks.txt')