from gensim.models import word2vec
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

sentences = word2vec.Text8Corpus('text8')
# train the skip-gram model; default window=5
model = word2vec.Word2Vec(sentences, size=200)
# ... and some hours later... just as advertised...
model.most_similar(positive=['woman', 'king'], negative=['man'], topn=1)
[('queen', 0.5359965)]
 
# pickle the entire model to disk, so we can load&resume training later
model.save('text8.model')
# store the learned weights, in a format the original C tool understands
model.save_word2vec_format('text8.model.bin', binary=True)

model.most_similar(['girl', 'father'], ['boy'], topn=3)
[('mother', 0.61849487), ('wife', 0.57972813), ('daughter', 0.56296098)]
more_examples = ["he his she", "big bigger bad", "going went being"]
for example in more_examples:
	a, b, x = example.split()
	predicted = model.most_similar([x, b], [a])[0][0]
	print "'%s' is to '%s' as '%s' is to '%s'" % (a, b, x, predicted)

# which word doesn't go with the others?
model.doesnt_match("breakfast cereal dinner lunch".split())
'cereal'
