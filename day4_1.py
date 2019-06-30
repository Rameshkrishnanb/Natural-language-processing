from textblob import TextBlob
from textblob import Word
import math
s1="water water everywhere nor a drop to drink"
s2="Two roads diverged by and i took the one roads less travelled"
sen1=TextBlob(s1)
sen2=TextBlob(s2)
d={}
for i in sen1.words:
	if i in d:
		d[i]+=1
	else:
		d[i]=1
for j in sen2.words:
	if j in d:
		d[j]+=1
	else:
		d[j]=1
print ("tdf")
print (d)
doc_list=[sen1,sen2]
i={}
for k in d.keys():
	idf=1+math.log(len(doc_list)/d[k])
	i[k]=round(idf,2)
print ("idf")
print (i)

for l in d.keys():
	if d[l]==max(d.values()):
		print (l)
	

