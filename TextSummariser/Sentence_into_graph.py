'''Here We want to create a graph from the sentence of a paragraph
'''
import matplotlib.pyplot as plt
import nltk
text="Any Random Text is taken Here. Random Text is taken Here.Any Text is taken Here.Any Random is taken Here.Any Random Text taken Here.Any Random Text is Here"
a=text.split('.')
#print(a)
Sentence_graph={}#Created an empty Dictionary
count=0

#Assignment of dictionary
for words in a:
    #print(words)
    temp=[]
    for word_1 in a:
        if(word_1 !=words):
            temp.append(word_1)
    #print(temp)
    Sentence_graph[words]=temp

print(Sentence_graph)
