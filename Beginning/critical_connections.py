from collections import defaultdict


def findcriticalnodes(n, edges):
    g = defaultdict(list)
    for conn in edges:
        g[conn[0]].append(conn[1])
        g[conn[1]].append(conn[0])
    visited = [0] * n
    isarticulationpoints = [0] * n
    order = [0] * n
    low = [0] * n
    seq = 0

    def dfs(u, p):
        nonlocal seq
        visited[u] = 1
        order[u] = low[u] = seq
        seq = seq + 1
        children = 0
        for to in g[u]:
            if to == p:
                continue
            if visited[to]:
                low[u] = min(low[u], low[to])
            else:
                dfs(to, u)
                low[u] = min(low[u], low[to])
                if order[u] <= low[to] and p != -1:
                    isarticulationpoints[u] = 1
                children += 1

        if p == -1 and children > 1:
            isarticulationpoints[u] = 1

    dfs(0, -1)
    ans = []
    for i in range(len(isarticulationpoints)):
        if isarticulationpoints[i]:
            ans.append(i)
    return ans


if __name__ == "__main__":
    a = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]
    print(findcriticalnodes(7, a))