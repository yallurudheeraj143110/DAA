def tsp(curr, visited, cost, dp):
    n = len(cost)
    if len(visited) == n:
        return cost[curr][0]
    key = (curr, tuple(visited))
    if key in dp:
        return dp[key]
    ans = float('inf')
    for i in range(n):
        if i not in visited:
            visited.append(i)
            total = cost[curr][i] + tsp(i, visited, cost, dp)
            ans = min(ans, total)
            visited.pop()
    dp[key] = ans
    return ans
def solveTSP(cost):
    dp = {}
    return tsp(0, [0], cost, dp)
cost = [
    [0, 10, 15, 20]
]
print(solveTSP(cost))