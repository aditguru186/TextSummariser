'''Here We want to create a graph from the words of a sentence
'''
import matplotlib.pyplot as plt
text="Any Random Text is taken Here"
a=text.split()
#print(a)
Word_graph={}#Created an empty Dictionary
count=0

#Assignment of dictionary
for words in a:
    temp=[]
    for word_1 in a:
        if(word_1 !=words):
            temp.append(word_1)
    Word_graph[words]=temp

print(Word_graph)
