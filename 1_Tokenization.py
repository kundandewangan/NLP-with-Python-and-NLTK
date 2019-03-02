import nltk
from nltk import sent_tokenize, word_tokenize
text="Hi Mr. KD. This is a demo. Get to wrk, dont loose hope."
#tokenize on the basis of sentences
print (sent_tokenize(text)) 
#tokenize on the basis of words
print (word_tokenize(text))