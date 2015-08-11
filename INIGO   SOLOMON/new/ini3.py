import json

from gensim.models import word2vec
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
#json.loads(unicode(opener.open('5'), "ISO-8859-1"))


sentences = word2vec.Text8Corpus('5')
model = word2vec.Word2Vec(sentences, size=200)
print model.most_similar(positive=['business','intelligence'], negative=['analysis'], topn=1)

