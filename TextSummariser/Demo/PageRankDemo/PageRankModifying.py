# -*- coding: cp1252 -*-
###implementing the page rank function after the similarity has been found
#Assigning edge weight values to the the graph,which is the similarity 
import networkx as nx
import matplotlib.pyplot as plt
import math
import re

graph=[]     #list of tupples of nodes
text_dict={}#text converted to dictionary form, where all the nodes are now represented by 0,1...,n
labels=[]
Edge_dict={}
PageRankProxy={}
PageRankSentences={}
#rank_sum=0
def draw_graph(graph, graph_layout='shell',
               node_size=1600, node_color='blue', node_alpha=0.3,
               node_text_size=12,
               edge_color='blue', edge_alpha=0.3, edge_tickness=1,
               edge_text_pos=0.3,
               text_font='sans-serif'):

    # create networkx graph
    G=nx.Graph()

    # add edges
    for edge in graph:
        G.add_edge(edge[0], edge[1])

    # these are different layouts for the network you may try
    # shell seems to work best
    graph_pos=nx.shell_layout(G)

    # draw graph
    nx.draw_networkx_nodes(G,graph_pos,node_size=node_size, alpha=node_alpha, node_color=node_color)
    nx.draw_networkx_edges(G,graph_pos,width=edge_tickness,alpha=edge_alpha,edge_color=edge_color)
    nx.draw_networkx_labels(G, graph_pos,font_size=node_text_size,font_family=text_font)

    #print(labels)
    edge_labels = dict(zip(graph, labels))
    nx.draw_networkx_edge_labels(G, graph_pos, edge_labels=edge_labels, label_pos=edge_text_pos)
    # show graph
    plt.show()

def preProcess(a):
    a=re.sub("�","'",a)
    a=re.sub("'",'',a)
    a=re.sub("/",' or ',a)
    a=re.sub('�','',a)
    a=re.sub('�','',a)
    a=re.sub('"','',a)
    a=re.sub("p.m",'pm',a)
    a=re.sub("a.m",'am',a)
    a=re.sub('�','',a)
    a=re.sub('�',"'",a)
    return a

def removeStopWords(text_list,stopWords):
    new_text=[]
    for sent in text_list:
        new_sent=sent.split(' ')
        new_sent1=[]
        for w in new_sent:
            w=w.strip('\'"?.,')
            val=re.search(r"[a-zA-Z][a-zA-Z0-9]*[a-zA-Z]+[a-zA-Z0-9]*$",w)
            if(w in stopWords or val is None):
                continue
            else:
                new_sent1.append(w.lower())
        new_text.append(new_sent1)
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

def Similarity(si,sj):
    len1,len2=len(si),len(sj)
    sim=0.0
    a1,a2=si.split(' '),sj.split(' ')
    similar_length=0
    for i in a1:
        for j in a2:
            if(i==j):
                similar_length+=1
    sim=similar_length/(math.log(len1)+math.log(len2))
    return round(sim,4)
    
def EvaluateEdge(a,n):
    for i in range(n-1):
        for j in range(i+1,n):
            temp=(i,j)
            sim=Similarity(a[i],a[j])
            Edge_dict[temp]=sim
            temp=(j,i)
            Edge_dict[temp]=sim
            labels.append(sim)

def PageRankFake(l,d,n):#(i,d,n)
    sum1,sum2,sum3=0.0,0.0,0.0
    for j in range (0,l):
        if(j!=n-1):
            for k in range(j+1,n):
                temp=(j,k)
                sum2+=Edge_dict[temp]
        else:
            sum2=1#forcefully assumed, the case in which the last node is reached and yet we dont know the value of the last edge
        temp=(l,j)
        if(sum2==0):
            sum2=1
        sum1+=(Edge_dict[temp] * PageRankProxy[j])/sum2
    sum3=(1-d)*d*(sum1)
    PageRankProxy[l]=sum3

def PageRankReal(l,d,n):#(i,d,n)
    sum1,sum2,sum3=0.0,0.0,0.0
    for j in range (0,l):
        if(j!=n-1):
            for k in range(j+1,n):
                temp=(j,k)
                sum2+=Edge_dict[temp]
        else:
            sum2=1#forcefully assumed, the case in which the last node is reached and yet we dont know the value of the last edge
        temp=(l,j)
        if(sum2==0):
            sum2=1
        sum1+=(Edge_dict[temp] * PageRankSentences[j])/sum2
    sum3=(1-d)*d*(sum1)
    PageRankSentences[l]=sum3
            

def EvaluatePageRank(n):
    d=0.5 # set some values between 0.0 to 1.0
    sum1=0.0
    for i in range(1,n):
        sum1+=Edge_dict[(0,i)]
    sum1=(1-d)*d*(sum1)
    PageRankProxy[0]=sum1#we have assumed the first node's PR value to be 1 and reevaluated on the same
    for i in range(1,n):
        PageRankFake(i,d,n)
    PageRankSentences[0]=PageRankProxy[0]
    for i in range(1,n):
        PageRankReal(i,d,n)
    #print(PageRankSentences)

def listFormInput(text):
    full_stop_sent=text.split('.')
    exclamation_sent=[]
    semicolon_sent=[]
    for i in full_stop_sent:
        temporary=i.split('!')
        for j in temporary:
            exclamation_sent.append(j)
    for i in exclamation_sent:
        temporary=i.split(';')
        for j in temporary:
            semicolon_sent.append(j)
    return semicolon_sent

def evaluateThreshold():
    rank_sum=0
    for i in range(len(PageRankSentences)):
        rank_sum+=(PageRankSentences[i]*PageRankSentences[i])
    thresh=rank_sum/len(PageRankSentences)
    thresh=math.sqrt(thresh)
    return thresh

def getInputText():
    with open('/Users/aguru/Desktop/AdiWorkspace/python/TextSummariser/TextSummariser/Demo/PageRankDemo/input.txt') as fp_input:
         mylist = [line.rstrip('\n') for line in fp_input]
    # fp_input = open('/Users/aguru/Desktop/AdiWorkspace/python/TextSummariser/TextSummariser/Demo/PageRankDemo/input.txt','r')
    input_text = """"""
    for i in mylist:
        input_text = input_text + " " + i
    fp_input.close()
    return input_text

def logOutputText(summary:str):
    try:
        with open('/Users/aguru/Desktop/AdiWorkspace/python/TextSummariser/TextSummariser/Demo/PageRankDemo/output.txt','w+t') as fp_output:
            summary = "\nThe Summary is : "+summary
            fp_output.write(summary)
    except Exception as e:
        print(e)


########
########'
########
# text=input('Enter the text to be summarised (within double Quotes):\n')
text = getInputText() 
text=preProcess(text)
#percentageThresh=input("Enter the Percentage to which the summarization is to be done:\t")
#print(text)
rank_sum=0
a=listFormInput(text)
del(a[len(a)-1])
#print(a)
n=len(a)
stopWords=getStopWords()
newTextList=removeStopWords(a,stopWords)
#print(newTextList)
a_noStop=[]# List containing the removed StopWords in list of sentences
for i in newTextList:
    stemp=""
    for  j in i:
        stemp+=j  +' '
    a_noStop.append(stemp.strip())
#print(a_noStop) #appending done, Works well
no_edges=int(n*(n-1)/2)
for i in range(n):
        text_dict[i]=a[i]
#'''#Here we are about to create the graph list, on which we will be computing the list of nodes available to us'''
#print(text_dict)
for i in range(n-1):
    for j in range(i+1,n):
        graph.append((i,j))

#defAGraph(n)
EvaluateEdge(a_noStop,n)
EvaluatePageRank(n)
#print(Edge_dict)
threshold=evaluateThreshold()#Setting the Threshold value
threshold=threshold*0.09
print ('\nSetting Threshold to be :',round(threshold,5))
summary=""
sum_count=0
sum_ratio=0.0
for i in range(n):
    if(PageRankSentences[i]>threshold):
        summary+=a[i]+'.'
        sum_count+=1
print("\nTHE SUMMARY OF THE TEXT IS OUT:\n")
# print(summary)
logOutputText(summary)
sum_ratio=(float(sum_count)/float(n))
print ('\nThe Summary ratio is :',round(sum_ratio,5))
draw_graph(graph, labels)
