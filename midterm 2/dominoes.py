"""
Juan Diego Valencia Alomia
Codigo: 8977467
"""

from sys import stdin


g = {}
p = []

n = 0
ans = False

def solve(u, vis, d, us):
    global ans
    if d == n:
        ans = u == us
    elif not ans and u in g:
        for i in g[u]:
            if not vis[i]:
                x, y = p[i]
                vis[i] = True
                if x == u and not ans:
                    solve(y, vis, d + 1, us)
                if y == u and x != y and not ans:
                    solve(x, vis, d + 1, us)
                vis[i] = False
                

def main():
    global g, n, p, ans
    c = 1
    n = int(stdin.readline().strip())
    while n != 0:   
        m = int(stdin.readline().strip())
        ui, vi = map(int, stdin.readline().split())
        us, vs = map(int, stdin.readline().split())
     
        g = {}
        p = []
       
        for i in range(m):
            u, v = map(int, stdin.readline().split())
            p.append((u, v))
            if u not in g:
                g[u] = []
            if v not in g:
                g[v] = []
            g[u].append(i)
            g[v].append(i)
        ans = False
        vis = {i : False for i in range(m)}   
        solve(vi, vis, 0, us)
        if ans:
            print("YES")
        else:
            print("NO")
        c += 1
        n = int(stdin.readline().strip())
    
main()