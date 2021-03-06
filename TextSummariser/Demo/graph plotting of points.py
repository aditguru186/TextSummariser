import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(graph):
    nodes=set([n1 for n1,n2 in graph] + [n2 for n1,n2 in graph])
    #print(nodes)
    G=nx.Graph()
    for node in nodes:
        G.add_node(node)
    for edge in graph:
        G.add_edge(edge[0],edge[1])
    pos=nx.shell_layout(G)
    nx.draw(G,pos)
    plt.show()


graph = [(20, 21),(21, 22),(22, 23), (23, 24),(24, 25), (25, 20)]
draw_graph(graph)



    
