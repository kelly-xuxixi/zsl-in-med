import scipy.io as sio
import numpy as np
from sklearn.metrics import average_precision_score
from config import cfg

y_true = sio.loadmat('/m/data/med/metadata/y_train.mat')
y_true = np.array(y_true['y_train'])
if cfg.eval_with_bg:
    y_true = np.vstack([y_true, np.zeros((4992, 20))])
y_rank = np.loadtxt('all_ranks.txt')
y_rank = np.transpose(y_rank)
print(np.isnan(y_true).any(), np.isnan(y_rank).any())
print(y_true.shape, y_rank.shape)
print(average_precision_score(y_true, y_rank))