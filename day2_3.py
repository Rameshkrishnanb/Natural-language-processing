
from textblob import TextBlob
from textblob import Word
sentence=raw_input("enter the sentence")
sent=TextBlob(sentence)
tag=sent.tags
for word,pos in tag:

	print (word+"- "+pos)
	

