from textblob import TextBlob
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


v=TfidfVectorizer(stop_words='english')
x=v.fit_transform(texts)
d=v.vocabulary_
print (d)
m={}
for key in d.keys():
	for i in texts:
		s=TextBlob(i)
		w=s.words
		for j in w:
			print(j +" j ");
			
			if j.lower()==key:
				print (j,key)
				if key in m:
					m[key]+=1
				
				else:
					m[key]=1
					

p=[]
r=[]
for km in d.keys():
	r=d.values()
	p.append(m[km])
X=zip(r,p)
print (X)
k=KMeans(n_clusters=2)
k.fit(X)
f=k.labels_
print (f)
import matplotlib.pyplot as plt
plt.scatter(m.keys(),m.values(),c=f)
plt.show()
