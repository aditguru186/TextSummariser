import networkx as nx
import matplotlib.pyplot as plt

graph=[]     #list of tupples of nodes
text_dict={}#text converted to dictionary form, where all the nodes are now represented by 0,1...,n

def draw_graph(graph, labels=None, graph_layout='shell',
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

    '''if labels is None:
        labels = range(len(graph))

    edge_labels = dict(zip(graph, labels))
    nx.draw_networkx_edge_labels(G, graph_pos, edge_labels=edge_labels, label_pos=edge_text_pos)'''

    # show graph
    plt.show()

########
########
########
text="Any Random Text is taken Here. Random Text is taken Here.Any Text is taken Here.Any Random is taken Here.Any Random Text taken Here.Any Random Text is Here"
a=text.split('.')
n=len(a)
no_edges=int(n*(n-1)/2)
for i in range(n):
        text_dict[i]=a[i]
#print(text)
'''Here we are about to create the graph list, on which we will be computing the list of nodes available to us'''
for i in range(n-1):
    for j in range(i+1,n):
        graph.append((i,j))

draw_graph(graph)
