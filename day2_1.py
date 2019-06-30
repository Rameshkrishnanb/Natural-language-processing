from textblob import TextBlob
from textblob import Word
noun=raw_input("enter the singular noun")
n=Word(noun)
print(n.pluralize())
