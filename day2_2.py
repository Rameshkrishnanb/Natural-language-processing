from textblob import TextBlob
from textblob import Word
#noun=raw_input("enter the plural noun")
noun=("apples")
temp=Word(noun) 
print(temp.singularize())
