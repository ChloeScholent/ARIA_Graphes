import networkx as nx
import matplotlib.pyplot as plt
import scipy as sp

n = 7236  #nodes
m = 22270 #edges

G = nx.gnm_random_graph(n, m)

# some properties
print("node degree clustering")
for v in nx.nodes(G):
    print(f"{v} {nx.degree(G, v)} {nx.clustering(G, v)}")

print()
print("the adjacency list")
for line in nx.generate_adjlist(G):
    print(line)

pos = nx.spring_layout(G)
nx.draw(G, pos=pos)
plt.show()

