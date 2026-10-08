def dfs(adj):
    V = len(adj)
    visited = [False] * V
    res = []
    src = 0
    stack = []

    visited[src] = True
    res.append(src)
    stack.append((src, iter(adj[src])))

    while stack:
        curr, neighbors = stack[-1]

        for i in neighbors:
            if not visited[i]:
                visited[i] = True
                res.append(i)
                stack.append((i, iter(adj[i])))
                break
        else:
            stack.pop()

    return res


graph = {
    0: [1, 5],
    1: [0, 2, 4, 3],
    2: [1, 4],
    3: [1, 4, 6],
    4: [1, 2, 3, 5],
    5: [0, 4],
    6: [3]
}

result = dfs(graph)
print(result)