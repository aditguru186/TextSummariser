#Text Frequency Model 2
#TFIDF implementation for a sample text
#Summarization to some extent
import math
import textblob
from textblob import TextBlob as tb
import re
import sys

#reload(sys)  
#sys.setdefaultencoding('utf8')

def preProcess(a):
    a=re.sub("’","'",a)
    a=re.sub("'",'',a)
    a=re.sub("/",' or ',a)
    a=re.sub('”','',a)
    a=re.sub('“','',a)
    a=re.sub('"','',a)
    a=re.sub("p.m",'pm',a)
    a=re.sub("a.m","am",a)
    a=re.sub("…",'.',a)
    return a

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


string=input('Enter the passage or document that needs to be summarised:\n')
string=preProcess(string)
input_text=tb(string)
#print(input_text.words)
stopWords=getStopWords()
newTextList=removeStopWords(input_text.words,stopWords)
#print(new_text)
#count=tf('stands',input_text)
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
strlen=len(input_list)
summary=""
sum_counter,sum_strlen=0,strlen
for i in sorted_words[:7]:#Manipulate the value so as to adjust the the length of your Summary
    flag=False
    for j in range(strlen):
        a=input_list[j].split(' ')
        for k in a:
            if(k.lower()==i[0]):
                summary+=input_list[j]+'.'
                sum_counter+=1
                del(input_list[j])
                strlen-=1
                flag=True
                break
        if(flag):
            break

print("\nThe Summary using Frequency:\n")
print(summary)

sum_ratio=float(sum_counter)/float(sum_strlen)
print "\nThe Summary ratio is: ",sum_ratio
