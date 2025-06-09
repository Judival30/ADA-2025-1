
"""
Juan Diego Valencia Alomia
codigo: 8977467
"""
from sys import stdin
from collections import deque



g= {}
ini, ext, c = 0, 0, 0
ways, waysVals = [], []

def coinsChange(target, coins):
    ans = float("inf")
    if target % 2 == 0:
        target //= 2 
        dp = [float('inf') for i in range(target + 1)] 
        dp[0] = 0
        for coin in coins:
            for i in range(coin, target + 1):
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        ans = dp[target] * 2
    return ans


def bfs(gr):
    global ways, waysVals
    dist = {i : float("inf") for i in gr}
    p = {i : -1 for i in gr}
    cost = {i : -1 for i in gr}  
    cost[ini] = 0
    dist[ini] = 0
    q = deque([(ini, 0)])
    flag = True
    while q and flag:
        u, curd = q.popleft()
        if u == ext:
            flag = False
        else:
            for v, w, in gr[u]:
                if curd + w < dist[v]:
                    dist[v] = curd + w
                    p[v] = u
                    cost[v] = w
                    q.append((v, curd + w))
  
    if dist[ext] != float("inf") and c - dist[ext] >= 0: 
        ways = []
        waysVals = []
        act = ext
        while act != ini:
            if act != ext:
                waysVals.append(cost[act])
            act = p[act]
       
        ans = coinsChange(c - dist[ext], waysVals)

    else:
        ans = dist[ext]
    return ans



def main():
    global g, ini, ext, c
    line = stdin.readline().strip()
    
    while line == "":
        line = stdin.readline().strip()
    t = int(line)
    for cs in range(t):
        line = stdin.readline().strip()
        while line == "":
            line = stdin.readline().strip()
        n, e = map(int,line.split())
        g = {i : [] for i in range(1, n + 1)}
        i = 0
        while i < e:
            line = stdin.readline().strip()
            if line != "":
                u, v, w = map(int, line.split())
                g[u].append((v, w))
                g[v].append((u, w))
                i += 1
        line = stdin.readline().strip()
        while line == "":
            line = stdin.readline().strip()
        k= int(line) 
        i = 0
        
        while i < k:
            line = stdin.readline().strip()
            if line != "":
                ini, ext, c = map(int, line.split())
                if ini in g and ext in g:
                    ans = bfs(g)
                    
                else:
                    ans = float("inf")
                if ans != float("inf"):
                    print("Yes %d" % (ans + len(waysVals) + 1))
                else:
                    print("No") 
                i += 1
        if cs < t - 1:
            print()
    
main()
