from textblob import TextBlob
from textblob import Word
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import numpy as np
texts = [
    'Timmy bought bright blue fishes.',
    'Timmy bought bright blue and orange bowl.',
    'The dog ate a fish at the store.',
    'Timmy went to the store. Timmy ate a bug. Timmy saw a fish.',
    'It meowed once at the bug, it is still barking at the bug and the fish',
    'The dog is at the fish store. The dog is orange. The dog is barking at the fish.',
    'Timmy is a fish.',
    'Timmy Timmy she loves fishes Timmy Timmy is no dog .',
    'The store is closed now.',
    'How old is that tree?',
    'I do not eat fish I do not eat dogs I only eat bugs.'
]


def freq(word):
	totfre = 0;
	for sent in texts:
		t	= TextBlob(sent);
		totfre = totfre + t.words.count(word);
	return totfre;


v=TfidfVectorizer(stop_words='english')
X=v.fit(texts)
d=v.vocabulary_
print (d);

print(d.keys());
for key in d.keys():
	print (key)
f = freq(Word('timmy'))
print (f)



