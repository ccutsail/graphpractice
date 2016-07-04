from networkx import *
import matplotlib.pyplot as plt

'''
This script simulates a basic example of the top trading cycle algorithm developed
by Shapley and Scarf in 1974. These graphs were used in my blog post from July 4,
2016.



'''

# initiate graph G and add nodes 
G = nx.DiGraph()
G.add_nodes_from ( [ 'A' ,'B' ,'C'],bipartite = 0)
G.add_nodes_from ( [ "A'","B'","C'"],bipartite = 1)

# I couldn't figure out how to use the actual bipartite method using l, r,
# so I just set l, r by hand. This won't work for larger graphs.

l = [ 'C' ,'B' ,'A']
r = [ "C'","B'","A'"]
G.add_edges_from([('A',"A'"),('B',"B'"),('C',"C'")]);

# This repositioning method is pulled from here:
# http://stackoverflow.com/questions/24829123/plot-bipartite-graph-using-networkx-in-python
pos = {}
# Update position for node from each group
pos.update((node, (1, index)) for index, node in enumerate(l))
pos.update((node, (2, index)) for index, node in enumerate(r))

# Original graph complete. Write to folder

networkx.write_graphml(G,"/Users/corycutsail/Desktop/graphpractice/TTCorg.graphml")
G = nx.read_graphml('/Users/corycutsail/Desktop/graphpractice/TTCorg.graphml')

# Create graph of original allocation

plt.figure(1)
nx.draw(G,pos,with_labels=True,node_color='white', text_font='sans-serif')
plt.show()

# Add cycle to represent exchange of A', B'

G.add_edges_from([("A'","B"),("B'","A"),('C',"C'")]);

green_edges = [("A'","B"),("B'","A")]

# This edge coloring method from here: 
# http://stackoverflow.com/questions/20133479/how-to-draw-directed-graphs-using-networkx-in-python
edge_colors = ['black' if not edge in green_edges else "#00ff00" for edge in G.edges()]

networkx.write_graphml(G,"/Users/corycutsail/Desktop/graphpractice/TTCcycle.graphml")
G = nx.read_graphml('/Users/corycutsail/Desktop/graphpractice/TTCcycle.graphml')


plt.figure(2)

nx.draw(G,pos,with_labels=True,node_color='white', 
               edge_color=edge_colors,
               text_font='sans-serif')
plt.show()

# The rest of this just repeats the process for the initial allocation for
# a second graph by swapping B' and A'. There is probably a better way to do this
# than hard-coding both of these, but because this is a small example I figured
# this works just as well. 

G2 = nx.DiGraph()
G2.add_nodes_from ( [ 'A' ,'B' ,'C'],bipartite = 0)
G2.add_nodes_from ( [ "A'","B'","C'"],bipartite = 1)

networkx.write_graphml(G2,"/Users/corycutsail/Desktop/graphpractice/TTCex2.graphml")
G2 = nx.read_graphml('/Users/corycutsail/Desktop/graphpractice/TTCex2.graphml')
G2.add_edge("A","B'",color='g');G2.add_edge("B","A'",color = 'g'); G2.add_edge('C',"C'");
l = [ 'C' ,'B' ,'A']
r = [ "C'","A'","B'"]
pos = {}
# Update position for node from each group
pos.update((node, (1, index)) for index, node in enumerate(l))
pos.update((node, (2, index)) for index, node in enumerate(r))
plt.figure(3)
nx.draw(G2,pos,with_labels=True,node_color='white')
plt.show()
