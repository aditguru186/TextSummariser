#TFIDF implementation for a sample text, done properly till Stopwords Removal
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

input_text=tb("""Tf-idf stands for term frequency-inverse document frequency, and the tf-idf weight is a weight often used in information retrieval and text mining. This weight is a statistical measure used to evaluate how important a word is to a document in a collection or corpus. The importance increases proportionally to the number of times a word appears in the document but is offset by the frequency of the word in the corpus. Variations of the tf-idf weighting scheme are often used by search engines as a central tool in scoring and ranking a documents relevance given a user query. One of the simplest ranking functions is computed by summing the tf-idf for each query term; many more sophisticated ranking functions are variants of this simple model.Tf-idf can be successfully used for stop-words filtering in various subject fields including text summarization and classification """)
#print(input_text.words)
stopWords=getStopWords()
new_text=removeStopWords(input_text.words,stopWords)
#print(new_text)
#count=tf('stands',input_text)
score={}
score={word: tf(word,input_text) for word in input_text.words}
#print(score)
