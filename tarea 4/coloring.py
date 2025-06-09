"""
Juan Diego Valencia Alomia
Codigo: 8977467
"""

from sys import stdin


g = {}
ans = []
kans = 0

def check(u, col, c):
    ans = True
    i = 0
    while i < len(g[u]) and ans:
        v = g[u][i]
        if col[v] == c :
            ans = False
        i += 1
    return ans
            
def solve(u, col, k):
    global ans, kans 
    if not(k + len(g) - u < kans):
        if u == len(g):
            if kans < k:
                kans = k
                ans = [i + 1 for i in range(len(col)) if col[i] == 1]
            elif kans == k:
                act = [i + 1 for i in range(len(col)) if col[i] == 1]
                flag = True
                i = 0
                
                while i < k and flag:
                    if act[i] < ans[i]:
                        flag = False
                        ans = act
                    elif act[i] > ans[i]:
                        flag = False    
                    i += 1  

        else:
            solve(u + 1, col, k)
            if check(u, col, 1):
                    col[u] = 1
                    solve(u + 1, col, k + 1)
                    col[u] = 0
                    


def main():
    global g, ans, kans
    t = int(stdin.readline().strip())
    for _ in range(t):
        n, e = map(int, stdin.readline().split())
     
        g = {i : [] for i in range(n)}
        col = [0 for i in range(n)]
        for i in range(e):
            u, v = map(int, stdin.readline().split())
            u -= 1
            v -= 1
            g[u].append(v)
            g[v].append(u)
  
        ans = []
        kans = 0
        solve(0, col, 0)
        print(kans)
        print(*ans) 


main()  
