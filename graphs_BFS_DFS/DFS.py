from graph_generator import GENERATE_GRAPH, VISUALIZE_GRAPH, \
                            MATRIX_TO_LIST, LIST_TO_MATRIX
import numpy as np
from math import inf
from graph_vertex_oop import Vertex, Graph

############################## tworzenie grafow ##########################

graph_matrix = GENERATE_GRAPH(5, 7)
VISUALIZE_GRAPH(graph_matrix)
new_graph = Graph(graph_matrix)


############################### BFS #######################################    
print_id = lambda x: print( str(id(x))[-3:] )

'''
Analiza czasu działania algorytmu:
    Dla każdego wierzchołka Grafa algorytm odwiedza rekurencyjnie wszystkie
    sąsiednie wierzchołki. Zatew w najgorszym przypadku DFS może odwiedzić 
    wszystkie wierzchołki i krawędzie w Grafie: O(V + E)
    V = liczba wierzchołków, E = liczba krawędzi 
'''

def DFS(G):
    
    def DFS_VISIT( G, v ):
        nonlocal time
        time += 1
        
        v.s = time
        v.color = 'grey'
        for u in G.adj_list[v] :
            if u.color == 'white':
                u.pi = v
                DFS_VISIT( G, u )
        time += 1
        v.m = time
        v.color = 'black'
        
    time = 0
    for v in G.adj_list :
        if v.color == 'white':
            DFS_VISIT( G, v )

DFS( new_graph )
print( new_graph )

for v in new_graph:
    print(v, v.color, v.pi, v.s, v.m)

