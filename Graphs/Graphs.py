import numpy as np

class Graph:

    def __init__(self, vertices):
        self._vertices = vertices # To initialize number of vertices in the graph
        self._adjMat = np.zeros((vertices, vertices))

    def insert_edge(self, u, v, w=1):
        self._adjMat[u][v] = w

    def remove_edge(self, u, v):
        self._adjMat[u][v] = 0
    
    def exist_edge(self, u, v):
        return self._adjMat[u][v] != 0

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
        for i in range(self._vertices):
            print(i, end=' ')
        print()
    
    def edges(self):
        for i in range(self._vertices):
            for j in range(self._vertices):
                if self._adjMat[i][j] != 0:
                    print(i, '---', j)
            print()
    
    def outdegree(self, u):
        count = 0
        for j in range(self._vertices):
            if self._adjMat[u][j] != 0:
                count += 1
        
        return count

    def indegree(self, v):
        count = 0
        for i in range(self._vertices):
            if self._adjMat[i][v] != 0:
                count += 1
        
        return count

    def display_adjMat(self):
        print(self._adjMat)

if __name__ == "__main__":
    G = Graph(4)

    print('Vertices: ', G.vertex_count())
    G.display_adjMat()
    print('Edges: ', G.edge_count(), '\n')

    G.insert_edge(0, 1)
    G.insert_edge(1, 0)

    G.insert_edge(0, 2)
    G.insert_edge(2, 0)

    G.insert_edge(1, 2)
    G.insert_edge(2, 1)

    G.insert_edge(2, 3)
    G.insert_edge(3, 2)
  

    G.display_adjMat()
    print('Edges count: ', G.edge_count(), '\n')

    # Display Edges
    print('Edges:')
    G.edges()

    #Check if an edge exists
    print('\n Existance of edge between 1 --- 2:', G.exist_edge(1, 2))
    print('\n Existance of edge between 1 --- 3:', G.exist_edge(1, 3))

    #Degree
    print('\n In-Degree of vertex 2: ', G.indegree(2))
    print('\n Out-Degree of vertex 2:', G.outdegree(2))