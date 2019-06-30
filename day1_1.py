from textblob import TextBlob
article="hello I am Blessy. I live in calicut. I did my BTECH in SCMS college. I worked as system Engineer in INFOSYS"
artblob=TextBlob(article)
s=artblob.sentences
print("-------------------sentence------------------------")
for i in s:
    print (i)
print("------------------words--------------------------")
for w in artblob.words:
	print (w)
print("--------------------nouns--------------------")
for n in artblob.noun_phrases:
	print (n)
