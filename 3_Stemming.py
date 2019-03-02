#reomoving suffix like parts from the words like removing 'ing' from swimming to get swim is STEMMING
from nltk import PorterStemmer 
from nltk import word_tokenize
ps=PorterStemmer()
egWords=["python", "pythoner", "pythoned", "pythoning", "pythoner", "pythonly", "swimming"]

'''for w in egWords:
    print(ps.stem(w))'''

sentence="Its very important to be pythonly while you are pythoning with python. All pythoners have puthoned poorely atleast once"


for w in word_tokenize(sentence):
    print(ps.stem(w))