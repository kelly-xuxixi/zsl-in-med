from util import Dict

cfg = Dict()
cfg.test = True
# get key words
cfg.use_tfidf = True
cfg.unify_synonyms = True
cfg.use_log_in_word_importance = True
cfg.delete_not_nones = True
cfg.delete_ambivalent_words = True
cfg.set_threshold = True
cfg.threshold = 2.3
# get concepts
cfg.use_word2vec = True
cfg.use_square_in_concept_selection = False