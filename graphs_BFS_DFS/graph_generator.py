import random
import numpy as np
import networkx as nx 
import matplotlib.pyplot as plt

############################# graf sgenerowany #############################

def GENERATE_GRAPH(n, k, directed=True):
    '''n = |V | i  k = |E|, p ∈ (0, 1)'''
    max_k = n*(n - 1)/2 
    if directed:
        max_k *= 2
        
    if not directed and k > max_k:
        raise ValueError(
            f"k ({k}) is greater then n*(n - 1)/2 ({n * (n - 1)//2})")
    elif directed and k > max_k:
        raise ValueError(
            f"k ({k}) is greater then n*(n - 1) ({n * (n - 1)})")
        
    if k >= max_k/2:
        ## idziemy z drugiej strony
        k = max_k - k  
        graph = np.ones( (n, n) ) - np.eye( n )
        empty_cell, full_cell = 1, 0
    else:
        graph = np.zeros( (n, n) )
        empty_cell, full_cell = 0, 1
        
    k_current = 0
    while k_current < k:
        u = random.randint(0, n - 1)
        v = random.randint(0, n - 1)

        if u != v and graph[u][v] == empty_cell:
            graph[u][v] = full_cell
            if not directed:
                graph[v][u] = full_cell  
            k_current += 1

    return graph

def VISUALIZE_GRAPH( graph ):
    edge_list = [ (i, j) for (i, j), value in np.ndenumerate(graph) if value]
    graph_visualizer = nx.DiGraph() 
    graph_visualizer.add_edges_from( edge_list ) 
    nx.draw_networkx( graph_visualizer ) 
    plt.show() 
    
n_vertices = 5
n_edges = 4
random_graph = GENERATE_GRAPH(n_vertices, n_edges, True)
# VISUALIZE_GRAPH( random_graph )
# print(random_graph)


################### graf losowy ####################
def GENERATE_RANDOM_GRAPH(n, probability, directed=True):
    if probability < 0 or probability > 1:
        raise ValueError(f"Probability ({probability}) ∉ [0, 1].")

    graph = np.zeros( (n, n) )

    for u in range(0, n):
        for v in range(u*(not directed), n):  
            if u != v and random.random() < probability:
                graph[u][v] = 1
                if not directed:
                    graph[v][u] = 1  
    return graph

n_vertices = 5
edge_probability = 1/2
random_graph = GENERATE_RANDOM_GRAPH(n_vertices, edge_probability, True)
# VISUALIZE_GRAPH(random_graph)
# print(random_graph)


##################### graph list ⇔	 graph matrix ####################

def MATRIX_TO_LIST(adj_matrix):
    adj_list = {  }
    n = len(adj_matrix)

    for row_index, row in enumerate( adj_matrix ):
        adj_list[ row_index ] = [ col_index 
                                       for col_index, col in enumerate(row) 
                                       if col]
    return adj_list

adj_list_graph = MATRIX_TO_LIST(random_graph)
# print(adj_list_graph)

def LIST_TO_MATRIX(adj_list):
    n = len(adj_list)
    graph_matrix = np.zeros( (n, n) )

    for vertex, neighbors in adj_list.items():
        for neighbor in neighbors:
            graph_matrix[vertex][neighbor] = 1

    return graph_matrix

matrix_graph = LIST_TO_MATRIX(adj_list_graph)
# print(matrix_graph)






