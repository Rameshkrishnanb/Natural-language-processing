from textblob import TextBlob
file=open('nlp.txt')
data=file.read()
print (data) 
sent=TextBlob(data)
print ("------------no of sentence------------")
print(len(sent.sentences))

print("--------------no of words-------------")
print(len(sent.words))

print("------------------- main words----------")
r=sent.sentences
print (r)

for i in r:
	tag=i.tags
	for word,pos in tag:
		if pos=='NN'or pos=='NNS':
			print (word)
print("------------summary---------------")
freq_table=dict()
non_list=list()
for k in r:
	t=k.tags
	for w,p in t:
		if p=='NN'or p=='NNS':
			if freq_table.has_key(w):
				freq_table[w]+=1
			else:
				freq_table[w]=1
average=sum(freq_table.values())/len(freq_table.values())
contents=[]
for k in r:
	t=k.tags
	for w,p in t:
		if p=='NN'or p=='NNS':
			if freq_table[w]>average:
				contents+=[k]

print(contents)
