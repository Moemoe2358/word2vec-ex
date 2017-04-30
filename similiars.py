# -*- coding: utf-8 -*-

import gensim.models.word2vec as word2vec
import sys

model   = word2vec.Word2Vec.load(sys.argv[1])
results = model.most_similar(positive=unicode(sys.argv[2], "utf-8"), topn=30)

for result in results:
    print result[0], '\t', result[1]