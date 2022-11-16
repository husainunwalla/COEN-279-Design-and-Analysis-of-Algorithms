#check if arbitrage exists
#Bellman Ford algorithm
#O(n^3) time complexity
#O(n) space complexity

def arbitrageBellmanFord(graph):
    #initialize the distance array
    dist = [0] * len(graph)
    #initialize the parent array
    parent = [None] * len(graph)
    #initialize the source vertex
    source = 0
    #initialize the destination vertex
    destination = None
    #initialize the number of vertices
    n = len(graph)
    #initialize the number of edges
    m = n * n
    #initialize the number of iterations
    k = n - 1
    #initialize the path array
    path = []
    #initialize the cycle array
    cycle = []

    #set the source vertex
    dist[source] = 1

    #relax the edges
    for i in range(k):
        for u in range(n):
            for v in range(n):
                if dist[u] * graph[u][v] > dist[v]:
                    dist[v] = dist[u] * graph[u][v]
                    parent[v] = u

    #check for negative cycles
    for u in range(n):
        for v in range(n):
            if dist[u] * graph[u][v] > dist[v]:
                destination = v
                break
        if destination is not None:
            break

    #check if destination is found
    if destination is not None:
        #find the cycle
        for i in range(n):
            destination = parent[destination]
        u = destination
        while True:
            cycle.append(u)
            u = parent[u]
            if u == destination:
                if len(cycle) > 1:
                    cycle.append(u)
                break
        #find the path
        if len(cycle) > 0:
            cycle.reverse()
            path = cycle
        #print the result
        print("Arbitrage exists")
        print("Path: " + " -> ".join([str(x) for x in path]))
        print("Amount: " + str(dist[destination]))
    else:
        print("Arbitrage does not exist")

#main
if __name__ == "__main__":
    #initialize the graph
    graphUSDRupeeYen = [
        [1, 64, 0],
        [0, 1, 1.8],
        [0.009, 0, 1]
    ]
    #find arbitrage
    arbitrageBellmanFord(graphUSDRupeeYen)