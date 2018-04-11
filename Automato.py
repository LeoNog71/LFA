from pygraph.classes.digraph import *

string =input("digite a seguido de b: ")

estados = ["q0","q1","q2","q3"]
estado_final = ["q0","q3"]
estado_inicial = "q0"
alfabeto = ["a","b"]


print("------------------------")
print("estados:")
print(estados)
print("------------------------")
print("estado inicial: "+estado_inicial)
print("------------------------")
print("estados finais: ")
print(estado_final)
print("------------------------")

grafo = digraph()

grafo.add_nodes(estados)
grafo.add_edge(("q0","q1"),label= alfabeto[0])
grafo.add_edge(("q0","q2"),label = alfabeto[1])
grafo.add_edge(("q1","q3"),label= alfabeto[0])
grafo.add_edge(("q1","q0"),label=alfabeto[1])
grafo.add_edge(("q2","q0"),label=alfabeto[0])
grafo.add_edge(("q2","q3"),label= alfabeto[1])
grafo.add_edge(("q3","q2"),label= alfabeto[0])
grafo.add_edge(("q3","q1"),label= alfabeto[1])

estado_atual = estado_inicial

while True:


    for x in string:

        a = grafo.neighbors(estado_atual)
        if a != None:

            for y in a:
                if grafo.edge_label((estado_atual,y)) == x:
                    print(estado_atual+"=>"+x)
                    estado_atual = y
                    print("=>"+y)
                    break





    if estado_atual == estado_final[0] or estado_atual == estado_final[1]:
        print("A sentença "+string+" pertence a linguagem")
        quit()
    else:
        print("Sentença "+string+" nao pertence a linguagem")
        quit()
