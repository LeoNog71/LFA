from pygraph.classes.graph import graph
from pygraph.algorithms.searching import breadth_first_search as bfs
g = graph()
g.add_node( "a" )
g.nodes()
g.add_node( "b" )
g.add_node( "c" )
g.add_node( "d" )
print(g.nodes())

g.add_edge( ("a","d") )
g.add_edge( ("b","d") )
g.add_edge( ("c","d") )
print(g.edges())

