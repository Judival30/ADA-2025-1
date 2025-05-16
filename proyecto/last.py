from sys import stdin
from time import perf_counter



dp = {}
but = []
n, m = 0, 0
mxd = 0


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def mx(a, b):
    return a if a > b else b

def mn(a, b):
    return a if a < b else b

def solve(r1, r2, t):
    if r1 < r2:
        r1, r2 = r2, r1 
    if t > mxd:
        t = mxd
    nb = r1 + 1
    k = (r1, r2, t)
    ans = None
    if k in dp:
        ans = dp[k]
    elif r1 == len(but) - 1:
        d = manhattan(but[r1], but[r2])
        ans = max(0, d - t)
        ans += 1
    else:
        d1 = manhattan(but[r1], but[nb])
        d2 = manhattan(but[r2], but[nb])
        nt1 = t + d1
        nt2 = max(0, d2 - t)
        a = solve(nb, r2, nt1) + d1
        b = solve(r1, nb, nt2) + nt2    
        ans = min(a, b)
    dp[k] = ans
   
    return ans
        

def main():
    global n, m, dp, but, mxd
    line = stdin.readline().strip()
    res = []
    while line != "": 
        n, m = map(int, line.split())
        q = int(stdin.readline().strip())
        but = [(1, 1)]
        for _ in range(q):
            i, j = map(int, stdin.readline().split())
            but.append((i, j))
        but.append((n, m))  
        mxd = manhattan((1, 1), (n, m))
        dp = {}
        ans = solve(0, 0, 0)
        res.append(str(ans))
        line = stdin.readline().strip()
    print("\n".join(res))



main()

