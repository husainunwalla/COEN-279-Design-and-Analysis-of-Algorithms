def arbitrageBellmanFord(graph):
    dist = [0] * len(graph)
    parent = [None] * len(graph)
    source = 0
    destination = None
    n = len(graph)
    m = n * n
    k = n - 1
    path = []
    cycle = []

    dist[source] = 1

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