from pygraph.classes.graph import *
estados = ["q0","q1","q2"]
grafo = graph()
grafo.add_nodes(estados)
print(grafo.nodes())
grafo.add_edge(("q0","q1"))
print(grafo.edges())