import heapq
def prim(graph):
    n = len(graph)
    visited = [False] * n
    pq = [(0, 0)]
    total_cost = 0
    while pq:
        w, v = heapq.heappop(pq)
        if visited[v]:
            continue
        visited[v] = True
        total_cost += w
        for neigh, e_w in graph[v]:
            if not visited[neigh]:
                heapq.heappush(pq, (e_w, neigh))
    return total_cost
graph = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8)],
    2: [(1, 3), (3, 4)],
    3: [(0, 6), (1, 8), (2, 4)]
}
print("minimum spanning tree cost:", prim(graph))