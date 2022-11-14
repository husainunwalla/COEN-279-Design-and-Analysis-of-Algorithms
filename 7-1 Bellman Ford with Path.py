# Bellman Ford that prints shortest path
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
    
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
    
    #Prints the shortest Path Weight
    def printArr(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("%d \t\t %d" % (i, dist[i]))
    
    #Prints the actual Shortest Path
    def printShortestPath(self, parent, j):
        if parent[j] == None:
            print(j, end=" ")
            return
        self.printShortestPath(parent, parent[j])
        print(j, end=" ")

    #Bellman Ford with SHortest Path
    def BellmanFordSP(self, src):
        dist = [float("Inf")] * self.V
        dist[src] = 0
        parent = [None] * self.V
        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    parent[v] = u
        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return
        self.printArr(dist)
        for i in range(self.V):
            print("Shortest Path from %d to %d is: " % (src, i), end=" ")
            self.printShortestPath(parent, i)
            print()

#Driver Code
g = Graph(5)
g.addEdge(0, 1, -1)
g.addEdge(0, 2, 4)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)
g.addEdge(3, 2, 5)
g.addEdge(3, 1, 1)
g.addEdge(4, 3, -3)

g.BellmanFordSP(0)
