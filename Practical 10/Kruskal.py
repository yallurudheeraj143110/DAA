def kruskal(vertices, edges):
    edges.sort(key=lambda edge: edge[2])
    groups = [{v} for v in vertices]
    mst = []
    cost = 0
    for i, j, weight in edges:
        grp_i = None
        grp_j = None
        for group in groups:
            if i in group:
                grp_i = group
            if j in group:
                grp_j = group
        if grp_i != grp_j:
            mst.append((i, j, weight))
            cost += weight
            grp_i.update(grp_j)
            groups.remove(grp_j)
    return mst, cost
vertices = ['A', 'B', 'C', 'D']
edges = [
    ('A', 'B', 1),
    ('A', 'C', 2),
    ('B', 'C', 3),
    ('C', 'D', 4),
    ('B', 'D', 5)
]
mst, cost = kruskal(vertices, edges)
print("Minimum Spanning Tree:", mst)
print("Minimum Cost:", cost)