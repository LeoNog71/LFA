from pygraph.classes.digraph import *
estados = ["q0","q1","q2"]
grafo = digraph()
grafo.add_nodes(estados)
print(grafo.nodes())
grafo.add_edge(("q0","q1"))
print(grafo.edges())
grafo.add_edge(("q0","q2"))

print(grafo.edges())
