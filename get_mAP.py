import scipy.io as sio
import numpy as np
from sklearn.metrics import average_precision_score

y_true = sio.loadmat('/m/data/med/metadata/y_train.mat')
y_rank = np.loadtxt('all_ranks.txt')
y_rank = np.transpose(y_rank)
print(y_true.shape, y_rank.shape)
print(average_precision_score(y_true, y_rank))