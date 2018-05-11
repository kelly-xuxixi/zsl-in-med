from util import Dict

cfg = Dict()
cfg.test = True
# get key words
cfg.use_tfidf = True
cfg.unify_synonyms = True
cfg.use_log_in_word_importance = True
# get concepts
cfg.use_word2vec = True
cfg.use_log_in_concept_selection = False