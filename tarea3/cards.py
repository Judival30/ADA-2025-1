from sys import stdin
import heapq


def dijkstra(g):
    dist = {i: float('inf') for i in g}
    dist[0] = 0
    pq = [(0, 0)]
    ans = 0
    while pq:
        curd, u = heapq.heappop(pq)
        for v, w in g[u]:
            if curd + w < dist[v]:
                if dist[v] != float("inf"):
                    ans -= dist[v]
                dist[v] = curd + w
                ans += dist[v]
                heapq.heappush(pq, (curd + w, v))
   
    return ans
    

def main():
    global g, gt
    t = int(stdin.readline().strip())
    for _ in range(t):
        n, e = map(int, stdin.readline().strip().split())
        gi = {i : [] for i in range(n)}
        gt = {i : [] for i in range(n)}
        for i in range(e):
            u, v, w, = map(int, stdin.readline().strip().split())
            u -= 1
            v -= 1
            gi[u].append((v, w))
            gt[v].append((u, w))
        ans = dijkstra(gi) + dijkstra(gt)
        print(ans)

main()