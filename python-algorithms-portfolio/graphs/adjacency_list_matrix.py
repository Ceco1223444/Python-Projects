import numpy as np
import typing
class AdjacencyList(object):
    @staticmethod
    def count_vertices_undirected_graph(
            adj_list: typing.Dict[int, typing.List[int]]) -> int:
        # for any graph the number of vertices equal to the number of keys.
        num_vertices = 0
        for vertex in adj_list.keys():
            num_vertices += 1
        return num_vertices
        
    @staticmethod
    def count_edges_undirected_graph(
            adj_list: typing.Dict[int, typing.List[int]]) -> int:
        # the number of edges is the sum of the len of the values divided by 2 as every edge is writte twice (UNDIRECTED).
        num_edges = 0
        for values in adj_list.values():
            num_edges += len(values)
        return num_edges // 2
    @staticmethod
    def count_vertices_directed_graph(
            adj_list: typing.Dict[int, typing.List[int]]) -> int:
        # for any graph the number of vertices equal to the number of keys.
        num_vertices = 0
        for vertex in adj_list.keys():
            num_vertices += 1
        return num_vertices
    @staticmethod
    def count_edges_directed_graph(
            adj_list: typing.Dict[int, typing.List[int]]) -> int:
        # the number of edges is the sum of the len of the values as every edge is writte only once (DIRECTED).
        num_edges = 0
        for values in adj_list.values():
            num_edges += len(values)
        return num_edges
      
    @staticmethod
    def count_odd_neighbours_undirected_graph(
            adj_list: typing.Dict[int, typing.List[int]]) -> int:
        # check each vertices how many edges it has, if it is odd number => neighbours are odd as well.
        num_odd_neighbours = 0
        for values in adj_list.values():
            if len(values) % 2 != 0:
                num_odd_neighbours += 1
        return num_odd_neighbours
    @staticmethod
    def list_to_matrix(
            adj_list: typing.Dict[int, typing.List[int]]) -> np.array:
        # create n x n matrix with the num of vertices and add "1" only if two vertices create edge.
        num_vertices = len(adj_list)
        adj_matrix = np.zeros((num_vertices, num_vertices))
        for i, neighbours in adj_list.items():
            for j in neighbours:
                adj_matrix[i][j] = 1
        return adj_matrix


    @staticmethod
    def count_vertices_directed_graph(adj_matrix: np.array) -> int:
       
        return len(adj_matrix)
    @staticmethod
    def count_edges_directed_graph(adj_matrix: np.array) -> int:
        
        return int(np.sum(adj_matrix))
    @staticmethod
    def count_odd_neighbours_undirected_graph(adj_matrix: np.array) -> int:
        
        num_odd = 0
        for i in range(len(adj_matrix)):
            if np.sum(adj_matrix[i]) % 2 != 0:
                num_odd += 1
        return num_odd
    @staticmethod
    def invert_directed_graph(adj_matrix: np.array) -> np.array:
        
        num_vertices = 0
        for i in range(len(adj_matrix)):
            num_vertices += 1
        
        new_matrix = np.zeros((num_vertices, num_vertices))
        
        for i in range(len(adj_matrix)):
            for j in range(len(adj_matrix[i])):
                new_matrix[j][i] = adj_matrix[i][j]
        
        return new_matrix
