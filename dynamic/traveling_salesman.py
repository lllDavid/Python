def tsp(dist):
    n = len(dist)
    dp = [[float('inf')] * n for _ in range(1 << n)]
    dp[1][0] = 0  

    for mask in range(1 << n):
        for u in range(n):
            if mask & (1 << u):
                for v in range(n):
                    if mask & (1 << v) == 0:
                        dp[mask | (1 << v)][v] = min(dp[mask | (1 << v)][v], dp[mask][u] + dist[u][v])

    return min(dp[(1 << n) - 1][i] + dist[i][0] for i in range(n))


dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
print(tsp(dist))  
