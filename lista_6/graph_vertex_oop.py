import numpy as np
from math import inf
from graph_generator import MATRIX_TO_LIST, LIST_TO_MATRIX

class Vertex():
    def __init__(self, index):
        self.index = index
        self.pi = None
        self.d = inf
        self.color = 'white'       
        
        self.m = 0
        self.s = 0
        
    def __repr__(self):
        return f"v{self.index}"
    
    def __str__(self):
        return f"v{self.index}"
    
class Graph():
    def __init__(self, graph_source, from_vertices=False):
        if from_vertices:
            self.adj_list = graph_source
            self.vertices_dict = {v.index: v for v in self.adj_list}
            self.graph_source = self.adj_list_to_dict(graph_source)
            self.adj_matrix = LIST_TO_MATRIX(self.graph_source)
        
        else:
            self.graph_source = graph_source
            self.create_adj_data()
            self.vertices_dict = {v: Vertex(v) for v in self.adj_list}
            self.adj_list = {
                self.vertices_dict[v] : [self.vertices_dict[v] for v in v_adj] 
                for v, v_adj in self.adj_list.items()             
                }
            
    def __getitem__(self, v_index):
        return self.vertices_dict[v_index]
    
    def __str__(self):
        return f"Adj List: {self.adj_list}"
    
    def __iter__(self):
        return iter( self.vertices_dict.values() )
        
    def create_adj_data(self):
        if type(self.graph_source) in [list, np.ndarray]:
            self.adj_matrix = np.array( self.graph_source )
            self.adj_list = MATRIX_TO_LIST(self.graph_source)
        elif type(self.graph_source) == dict:
            self.adj_matrix = LIST_TO_MATRIX(self.graph_source)
            self.adj_list = self.graph_source 
        else:
            raise TypeError(f'Cant create graph from {type(self.graph_source)}. '
                            +'Use <list> or <dict> instead!')
            
    def adj_list_to_dict(self, vertices):
        vertices_dict = { v.index : [v.index for v in v_adj] 
            for v, v_adj in vertices.items() }   
        return vertices_dict
    
    def reset_vertices(self):
        pass
    
    def create_undirected(self):
        pass
    
    