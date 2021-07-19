"""
an adjacency list is a method to store a directed or undirected graph 
associates each vertex in the graph with the collection of its neighboring 
vertices or edges.
for more description : https://en.wikipedia.org/wiki/Adjacency_list
"""
import unittest
from linked_list import LinkedList, Item

class ADJList():

    def __init__(self) -> None:       
        self._lenght = 0
        self._labels_list = {}

    def labels(self) -> list:
        labels = self._labels_list.keys()
        return labels

    def neighbors(self, x) -> list:     
        neighbors = self._labels_list[x].ids()
        return neighbors

    def add(self, x, y) -> None:    
        neighbor = Item(y, None)
        if x in self._labels_list:
            self._labels_list[x].insert(neighbor)
        else:
            neighbors_lst = LinkedList() # init the list of neighbors of x as a linked list.
            neighbors_lst.insert(neighbor)
            self._labels_list[x] = neighbors_lst

    def __repr__(self) -> str:
        pass


class Graph():

    def __init__(self) -> None:
        self._edges = 0
        self._vertexes = 0
        self._adj_lst = ADJList()

    def edges_num(self):
        return self._edges

    def vertexes_num(self):
        return self._vertexes

    def __repr__(self) -> str:
        rep = ""
        labels = self._adj_lst.labels()
        for label in labels:
            neighbors = self._adj_lst[label].ids(label)
            rep += str(label) + "->" + str(neighbors)
        return rep
    
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
            self._vertexes, self._edges = file.readline().split()
            self._vertexes, self._edges = int(self._vertexes), int(self._edges)
            
            for line in file.readlines():
                x, y = line.split()
                x, y = int(x), int(y)
                self._adj_lst.add(x, y)

class TestGraph(unittest.TestCase):
    """
    graph.txt
    4 6
    1 2
    1 4
    1 4
    2 3
    3 2
    4 4
    """
    def setUp(self) -> None:
        self._graph = Graph()

    def test_create_graph(self):
        self._graph.create_graph("graph.txt")
        vertexes_num = self._graph.vertexes_num()
        edges_num = self._graph.edges_num()
        self.assertEqual(vertexes_num, 4)
        self.assertEqual(edges_num, 6)
        #self.assertEqual(repr(self._graph),90)

class TestADJList(unittest.TestCase):
    pass

if __name__ == "__main__":
    unittest.main()




