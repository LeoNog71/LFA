from pygraph.classes.digraph import *
from pygraph.algorithms.searching import *

string =input("digite a seguido de b: ")

estados = ["q0","q1","q2","q3"]
estado_final = ["q0","q3"]
estado_inicial = "q0"
alfabeto = ["a","b"]

print("estados:")
print(estados)
print("estado inicial: "+estado_inicial)
print("estados finais: ")
print(estado_final)
print("------------------------")
grafo = digraph()

grafo.add_nodes(estados)

grafo.add_edge(("q0","q1"),label= alfabeto[0])
grafo.add_edge(("q1","q0"),label = alfabeto[0])
grafo.add_edge(("q1","q3"),label= alfabeto[1])
grafo.add_edge(("q0","q2"),label=alfabeto[1])
grafo.add_edge(("q2","q3"),label=alfabeto[1])
grafo.add_edge(("q3","q2"),label= alfabeto[1])

estado_atual = estado_inicial
T = False
while not T:

    for x in string:

        a = grafo.neighbors(estado_atual)

        for y in a:
            if grafo.edge_label((estado_atual,y)) == x:
                print(estado_atual+"=>"+x)
                estado_atual = y
                print("=>"+y)




    if estado_atual == estado_final[0] or estado_atual == estado_final[1]:
        print("A sentença "+string+" pertence a linguagem")
        T = True
    else:
        print("Sentença nao pertence a linguagem")
        quit()
