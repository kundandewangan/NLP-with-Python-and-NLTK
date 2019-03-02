from nltk.corpus import stopwords
from nltk import word_tokenize

sentence="This is an example for the various stop words."

#set of english words that is predefined by nltk
stopWords=set(stopwords.words("english"))
    #print (stopWords)

words=word_tokenize(sentence)
filter=[]

for i in words:
    if i not in stopWords:
        filter.append(i)
print(filter)

'''one line code 
each word in word if w not in stopWord
    filter=[w for w in words if not w in stopWords]
    print(filter)'''