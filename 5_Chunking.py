#Chunking 
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
            #'.' represents any new character except a new line, ? is for 0 or 1, * means 0 or more, RB is adverb, VB is verb, NNP, is Proper noun, NN is noun, to mention any parts of speech tag we use <>, r means to perform a regex may be its not necessary to put r, I will confirm that. the name used here 'Chunk' can be any name. 
            chunkGram= r"""Chunk: {<RB.?>*<VB.?>*<NNP><NN>?} """
            chunkParser= nltk.RegexpParser(chunkGram)
            #tagged contains all the parts of speech, so chunking tagged
            chunked=chunkParser.parse(tagged)
            #print (chunked)

            #drawing the representation through matplotlib
            chunked.draw()
    except Exception as e:
        print(str(e))

process()
