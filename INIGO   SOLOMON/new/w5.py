from __future__ import unicode_literals
import os
import nltk
directories = ['train/pos', 'train/neg', 'test/pos', 'test/neg', 'train/unsup']
input_file = open('/home/sanjyot/Downloads/alldata.txt', 'w')
id_ = 0
for directory in directories:
    rootdir = os.path.join('/home/sanjyot/Downloads/aclImdb', directory)
    for subdir, dirs, files in os.walk(rootdir):
        for file_ in files:
            with open(os.path.join(subdir, file_), 'r') as f:
                doc_id = '_*%i' % id_
                id_ = id_ + 1

                text = f.read()
                text = text.decode('utf-8')
                tokens = nltk.word_tokenize(text)
                doc = ' '.join(tokens).lower()
                doc = doc.encode('ascii', 'ignore')
                input_file.write('%s %s\n' % (doc_id, doc))
input_file.close()
