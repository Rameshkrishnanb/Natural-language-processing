from textblob import TextBlob
article="good mornind,always be the reson that someone smiles today"
   blob=TextBlob(article)
print(blob.correct())
print(blob.translate(to="es"))
