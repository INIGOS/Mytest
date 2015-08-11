class BrownCorpus(object):

	def __init__(self, dirname):
		self.dirname = dirname
 
	def __iter__(self):
	for fname in os.listdir(self.dirname):
		fname = os.path.join(self.dirname, fname)
		if not os.path.isfile(fname):
			continue
		for line in open(fname):
                 # each file line is a single sentence in the Brown corpus
                 # each token is WORD/POS_TAG
			token_tags = [t.split('/') for t in line.split() if len(t.split('/')) == 2]
                 # ignore words with non-alphabetic tags like ",", "!" etc (punctuation, weird stuff)
			words = ["%s/%s" % (token.lower(), tag[:2]) for token, tag in token_tags if tag[:2].isalpha()]
			if not words:  # don't bother sending out empty sentences
				continue
			yield words
