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
    currentpath = '/Users/aguru/Desktop/AdiWorkspace/python/TextSummariser/TextSummariser/Demo/'
    fp=open((currentpath+'stopwords.txt'),'r')
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

def getInputText():
    with open('/Users/aguru/Desktop/AdiWorkspace/python/TextSummariser/TextSummariser/Demo/TextFrequencyDemo/input.txt','r') as fp_input:
         mylist = [line.rstrip('\n') for line in fp_input]
    # fp_input = open('/Users/aguru/Desktop/AdiWorkspace/python/TextSummariser/TextSummariser/Demo/PageRankDemo/input.txt','r')
    input_text = """"""
    for i in mylist:
        input_text = input_text + " " + i
    fp_input.close()
    return input_text

def logOutputText(summary:str):
    try:
        with open('/Users/aguru/Desktop/AdiWorkspace/python/TextSummariser/TextSummariser/Demo/TextFrequencyDemo/output.txt','w+t') as fp_output:
            summary = "\nThe Summary is : "+summary
            fp_output.write(summary)
    except Exception as e:
        print(e)

#########
#########
#########
        
input_string2 = getInputText()
input_text_blob=tb(input_string2)
stopWords=getStopWords()
newTextList=removeStopWords(input_text_blob.words,stopWords)
score={}
new_text=""
for i in newTextList:
    new_text+=i+' '
newText=tb(new_text)#Stop Words Eliminated list
score={word: tf(word,newText) for word in newText.words}
sorted_words = sorted(score.items(), key=lambda x: x[1], reverse=True)#returns a list of tupples of the sorted words found in the dictionary

input_list=input_string2.split('.')
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

logOutputText(summary)
print('Summary of text is out\n')
