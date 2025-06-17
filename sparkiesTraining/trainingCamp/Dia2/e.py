from sys import stdin
from collections import deque

cord = [(1, 0), (0, 1), (-1, 0), (0, -1)]
G = []
n, m = 0, 0
def escape(u):
    x, y, doors = u

    ans = False
    if  0 > x or  x >= n or 0 > y or y >= m:
        ans = True
    return ans

def new_state(u, dirm):
    x, y, doors = u
    xi, yi = dirm
    

    if G[x][y] == "C":
        doors = False
    elif G[x][y] == "O":
        doors = True
    
    xk, yk = x + xi, y + yi
    w = (xk, yk, doors)
    if  0 <= xk < n and 0 <= yk < m:
        if G[xk][yk] == "W":
            w =  None
        elif G[xk][yk] == "D" and not doors:
            w = None 
    #else: w = None
    return w 

def bfs(s):
    visited = set()
    q = deque(); q.append((s, 0))
    ans = -1
    while len(q) != 0 and ans == -1:
        u, d = q.popleft()
        #print(u)
        if escape(u):
            ans = d
        else:
            for dirm in cord:
                v = new_state(u, dirm)
                if v != None and  v not in visited:
                    visited.add(v)
                    q.append((v, d+1))
    return ans

def main():
    global G, n, m
    n, m = map(int, stdin.readline().split())
    while n != -1:
        G = []
        s = tuple()
        for i in range(n):
            line = stdin.readline().strip()
            for j in range(len(line)):
                if line[j] == 'H':
                    s = (i, j)
            G.append(line)
        ans = bfs((s[0], s[1], False))
        print(ans)
        n, m = map(int, stdin.readline().split())

main()