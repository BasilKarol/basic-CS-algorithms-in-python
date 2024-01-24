from graph_generator import GENERATE_GRAPH, VISUALIZE_GRAPH, \
                            MATRIX_TO_LIST, LIST_TO_MATRIX
import numpy as np
from math import inf
from graph_vertex_oop import Vertex, Graph

############################## tworzenie grafow ##########################

graph_matrix = GENERATE_GRAPH(10, 17)
VISUALIZE_GRAPH(graph_matrix)

new_graph = Graph(graph_matrix)
vertex_0 = new_graph[0]
# print( new_graph )

############################### BFS #######################################

'''
Analiza czasu działania algorytmu:
    Algorytm odwiedza wszystkie wierzchołki na każdym poziomie Grafu przed 
    przejściem do następnego poziomu. Zatew w najgorszym przypadku BFS może 
    odwiedzić wszystkie wierzchołki i krawędzie w Grafie: O(V + E)
    V = liczba wierzchołków, E = liczba krawędzi 
'''

def BFS(G, s):        
        s.d = 0
        s.color = 'grey'
        Q = [s]
        BFS_tree_list = {v:[] for v in G.adj_list}
        
        while Q:
            u = Q.pop( 0 )
            
            for v in G.adj_list[u]:
                if v.color == 'white':
                    v.pi = u
                    v.d = u.d+1
                    v.color = 'grey'
                    Q.append( v )
                    BFS_tree_list[u].append( v )
                    BFS_tree_list[v].append( u )  ##undirected
                    
            u.color = 'black'
        return BFS_tree_list

BFS_tree_0 = BFS( new_graph, vertex_0 )
Graph_tree_0 = Graph( BFS_tree_0, from_vertices=True )
# print(Graph_tree_0)
VISUALIZE_GRAPH( Graph_tree_0.adj_matrix )
# print(Graph_tree_0.adj_matrix)


##################### najkrótsza ścieżka ###############################

def PRINT_PATH( G, s, v ): 
    "przeszukiwanie najkrotszej sciezki juz PO zrobieniu BFS"
    if v == s:
        print( s )
    elif v.pi == None:
        print( "Nie ma sciezki" )
    else:
        PRINT_PATH( G, s, v.pi )
        print( v )
        
PRINT_PATH( Graph_tree_0, Graph_tree_0[0], Graph_tree_0[] )
