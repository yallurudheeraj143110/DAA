INF = float('inf')
dist = [
    [0, 3, 10, INF],
    [INF, 0, 1, 7],
    [INF, INF, 0, 2],
    [INF, INF, INF, 0]
]
V = len(dist)

for k in range(V):
    for i in range(V):
        for j in range(V):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
for row in dist:
    print(row)