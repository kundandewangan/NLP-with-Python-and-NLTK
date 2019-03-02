import nltk 
from nltk.corpus import state_union
''' PunktSentenceTokenizer is unsupervised ml sentence tokenizer 
It comes with pretraining and we can also further train it '''
from nltk import PunktSentenceTokenizer

train=state_union.raw("2005-GWBush.txt")
text=state_union.raw("2006-GWBush.txt")
SentenceTokenizer= PunktSentenceTokenizer(train)

tokenized=SentenceTokenizer.tokenize(text)

def process():
    try:
        for i in tokenized:
            words=nltk.word_tokenize(i)
            tagged=nltk.pos_tag(words)
            print(tagged)
    except Exception as e:
        print(str(e))
process()
