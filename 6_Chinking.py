#Chinking is based on chunking. We chink or remove something from the chunk 
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
            #   print(tagged)
            #'.' represents any new character except a new line, * means 0 or more, + means 1 or more than one, to mention any parts of speech tag we use <>, r means to perform a regex may be its not necessary to put r, I will confirm that. the name used here 'Chunk' can be any name. 

            #<.*>+ means chunk everything
            # '}{'  is used for chinking
            chunkGram= r"""Chunk: {<.*>+} 
                            }<VB.?| IN| DT>+{"""     # IN means Preposition and DT means Determiners, | means or 
            chunkParser= nltk.RegexpParser(chunkGram)
            #tagged contains all the parts of speech, so chunking tagged
            chunked=chunkParser.parse(tagged)
            print (chunked)

            #drawing the representation through matplotlib
            chunked.draw()
    except Exception as e:
        print(str(e))

process()
