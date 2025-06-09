"""
Juan Diego Valencia Alomia
Codigo: 8977467
"""

from sys import stdin

p, size = {}, {}

def find(u):
    if p[u] != u:
        p[u] = find(p[u])
    return p[u]

def union(ru, rv):
    if size[ru] < size[rv]:
        ru, rv = rv, ru
    p[rv] = ru
    size[ru] += size[rv]
     

def solve(g, n, lg):
    global p, size
    p = {i : i for i in range(1, n + 1)}
    size = {i : 1 for i in range(1, n + 1)}
    ans = 0
    for i in range(len(g)):
        w, u, v = g[i]
        w = abs(w)
        ru = find(u)
        rv = find(v)
        if ru != rv:
            union(ru, rv)
            nr = find(u)
            flag = True
            mx = 0
            mi = float("inf")
           
            j = 1
            while j <= n and flag:
                rj = find(j)
                if rj == nr:
                    k = 0
                    while k < len(lg[j]) and flag:
                        nk, wk = lg[j][k]
                        rk = find(nk)
                        if rk == nr:
                            mi = min(mi, wk)
                        else:
                            mx = max(mx, wk)
                        if mi <= mx:
                            flag = False
                        k += 1
                j += 1
                
            if size[nr] > 1 and mi > mx:
                ans += size[nr]
    
      
    return ans

def main():
    t = int(stdin.readline().strip())
    for _ in range(t):
        n, e = map(int, stdin.readline().strip().split())
        g = []
       
        lg = {i : [] for i in range(1, n + 1)}
        for i in range(e):
            u, v, w = map(int, stdin.readline().strip().split())
            
            lg[u].append((v, w))
            lg[v].append((u, w))
            g.append((-w, u, v))
        g.sort()

        print("%d" % solve(g, n, lg))
        
        
main()

