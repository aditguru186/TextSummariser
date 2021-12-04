#Text Frequency Model 2
#TFIDF implementation for a sample text
import math
import textblob
from textblob import TextBlob as tb
import re

def removeStopWords(text_list,stopWords):
    new_text=[]
    for w in text_list:
        w=w.strip('\'"?.,')
        val=re.search(r"[a-zA-Z][a-zA-Z0-9]*[a-zA-Z]+[a-zA-Z0-9]*$",w)
        if(w in stopWords or val is None):
            continue
        else:
            new_text.append(w.lower())

    return new_text

def getStopWords():
    fp=open('stopwords.txt','r')
    line=fp.readline()
    stop_words=[]
    while line:
        w=line.strip()
        stop_words.append(w)
        line=fp.readline()
    fp.close()
    return stop_words

def tf(word, blob):
    return (float)(blob.words.count(word)) / (float)(len(blob.words))

string="""Tf-idf stands for term frequency-inverse document frequency, and the tf-idf weight is a weight often used in information retrieval and text mining. This weight is a statistical measure used to evaluate how important a word is to a document in a collection or corpus. The importance increases proportionally to the number of times a word appears in the document but is offset by the frequency of the word in the corpus. Variations of the tf-idf weighting scheme are often used by search engines as a central tool in scoring and ranking a documents relevance given a user query. One of the simplest ranking functions is computed by summing the tf-idf for each query term; many more sophisticated ranking functions are variants of this simple model.Tf-idf can be successfully used for stop-words filtering in various subject fields including text summarization and classification """
input_text=tb("""Tf-idf stands for term frequency-inverse document frequency, and the tf-idf weight is a weight often used in information retrieval and text mining. This weight is a statistical measure used to evaluate how important a word is to a document in a collection or corpus. The importance increases proportionally to the number of times a word appears in the document but is offset by the frequency of the word in the corpus. Variations of the tf-idf weighting scheme are often used by search engines as a central tool in scoring and ranking a documents relevance given a user query. One of the simplest ranking functions is computed by summing the tf-idf for each query term; many more sophisticated ranking functions are variants of this simple model.Tf-idf can be successfully used for stop-words filtering in various subject fields including text summarization and classification """)
stopWords=getStopWords()
newTextList=removeStopWords(input_text.words,stopWords)
score={}
new_text=""
for i in newTextList:
    new_text+=i+' '
newText=tb(new_text)#Stop Words Eliminated list
score={word: tf(word,newText) for word in newText.words}
#print(score)
sorted_words = sorted(score.items(), key=lambda x: x[1], reverse=True)#returns a list of tupples of the sorted words found in the dictionary
#print(sorted_words)

input_list=string.split('.')
strlen,point=len(input_list),0
summary=""
for i in sorted_words[:5]:
    flag=False
    for j in range(strlen):
        a=input_list[j].split(' ')
        for k in a:
            if(k.lower()==i[0]):
                summary+=input_list[j]+'.'
                del(input_list[j])
                strlen-=1
                flag=True
                break
        if(flag):
            break

print(summary)
