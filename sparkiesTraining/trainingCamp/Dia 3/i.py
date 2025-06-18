from sys import stdin
from collections import deque

def bfs(G, auti, n, A):
    dist = [-1 for i in range(n + 1)]
    q = deque([1])
    dist[1] = 0
    visA = [False for i in range(A + 1)]
    while q:
        u = q.popleft()
        d = dist[u]
        for a in G[u]:
            if not visA[a]:
                visA[a] = True
                for v in auti[a]:
                    if dist[v] == -1:
                        dist[v] = d +1
                        q.append(v)
    res = [d for d in dist[1:] if d != -1]
    D = len(res)
    M = sum(res)
    S = max(res)
    print(D, S, M)

def main():
    a, n = map(int, stdin.readline().split())
    G = {i : [] for i in range(n +1)}
    auti = []
    for i in range(a):
        lst = list(map(int, stdin.readline().split()))
        for p in lst[1:]:
            G[p].append(len(auti))
        auti.append(lst[1:])
    bfs(G, auti, n, a)     


main()