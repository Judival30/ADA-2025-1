"""
Juan Diego Valencia Alomia
Codigo: 8977467
"""

from sys import stdin
from sys import setrecursionlimit

setrecursionlimit(10**6)

ans = 0
m = 0
g = {}

def dfs(u, vis, d):
    global ans, g
    if d > ans:
        ans = d
    if ans < m:
        for v, i in g[u]:
            if not vis[i]:
                vis[i] = True
                dfs(v, vis, d + 1)
                vis[i] = False


def main():
    global ans, g, m
    n, m = map(int, stdin.readline().split())
    while n != 0 and m != 0:
        g = {i : [] for i in range(n)}
        
        for i in range(m):
            u, v = map(int, stdin.readline().split())
            g[u].append((v, i))
            g[v].append((u, i))
        ans = 0
        i = 0
        flag = True
        while i < n and flag:
            vis = [False for i in range(m)]
            dfs(i, vis, 0)
            if ans == m:
                flag = False
            i += 1
        print(ans)
        n, m = map(int, stdin.readline().split())

main()