"""
an adjacency list is a method to store a directed or undirected graph 
associates each vertex in the graph with the collection of its neighboring 
vertices or edges.
description : https://en.wikipedia.org/wiki/Adjacency_list
"""
from linked_list import *

class ADJList():

    def __init__(self) -> None:
        
        self._lenght = 0
        self._labels_list = {}

    def set_lenght(self, vertexes_num : int) -> None:
        self._lenght = vertexes_num

class Graph():

    def __init__(self) -> None:

        self._edges = 0
        self._vertexes = 0
        self._adj_lst = ADJList()

    def edges_num(self):
        return self._edges

    def vertexes_num(self):
        return self._vertexes

    def create_graph(self, txt_file) -> None:
        """
        for example directed graph:
            4 6 # in the first line 4 is meant for the number of nodes and 6 for the number of edges.
            1 2 # 1->2
            1 4 # 1->4
            1 4 # 1->4
            2 3 # 2->3
            3 2 # 3->2
            4 4 # 4->4 here is meant for loop in graph.
        """
        with open(txt_file) as file:

            self._vertexes, self._edges = file.readline().split("\t")
            self._vertexes, self._edges = int(self._vertexes), int(self._edges)
            self._adj_lst.set_lenght(self._vertexes)
            
            for line in file.readlines():
                x, y = line.split("/t")
                x, y = int(x), int(y) # x -> y.


