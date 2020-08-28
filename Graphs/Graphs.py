import numpy as np

class Graph:

    def __init__(self, vertices):
        self._vertices = vertices
        self._adjMat = np.zeros((vertices, vertices))

    def insert_edge(self, u, v, w=1):
        self._adjMat[u][v] = w

    def remove_edge(self, u, v):
        self._adjMat[u][v] = 0
    
    def exist_edge(self, u, v):
        return self._adjMat != 0

    def vertex_count(self):
        return self._vertices
        
    def edge_count(self):
        count = 0
        for i in range(self._vertices):
            for j in range(self._vertices):
                if self._adjMat[i][j] != 0:
                    count += 1
        
        return count

    def allvertices(self):
        for i in range(self._vertives):
            print(i, end=' ')
        print()
    
    def edges(self):
        for i in range(self._vertices):
            for j in range(self._vertices):
                print(i, '---', j)
            print()
    
    def outdegree(self, u):
        count = 0
        for j in range(self._vertices):
            if self._adjMat[v][j] != 0:
                count += 1
        
        return count

    def indegree(self, v):
        count = 0
        for i in range(self._vertices):
            if self._adjMat[i][v] != 0:
                count += 1
        
        return count