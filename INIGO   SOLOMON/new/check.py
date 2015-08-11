from gensim.models import word2vec
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',level=logging.INFO)
sentences=word2vec.Text8Corpus('/home/sanjyot/Desktop/INIGO/text8')
#model=word2vec.Word2vec(sentences,size=200)
model = word2vec.Word2Vec.load_word2vec_format('/home/sanjyot/Desktop/INIGO/GoogleNews-vectors-negative300.bin', binary=True)
#print model
print sentences
