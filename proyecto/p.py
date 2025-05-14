from sys import stdin

dp = {}
but = []
n, m = 0, 0
S = 0

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def solve(r1, r2, t1, t2):
    ans = float("inf")
    act = max(r1, r2)
    k = (r1, r2, t1, t2)
    if k in dp:
        ans = dp[k]
        print("solpao", k)
    elif act == len(but) - 1:
        ans = max(t1 + manhattan(but[r1], but[act]), t2 + manhattan(but[r2], but[act]))
    else:
        d1, d2 = manhattan(but[r1], but[act + 1]), manhattan(but[r2], but[act + 1])
        nt1, nt2 = max(t1 + d1, t2), max(t2 + d2, t1)
        ans = min(solve(act + 1, r2, nt1, t2), solve(r1, act + 1, t1, nt2))
    dp[k] = ans
    return ans



def main():
    global n, m, dp, but
    line = stdin.readline().strip()
    while line != "":
        
        n, m = map(int, line.split())

        q = int(stdin.readline().strip())
        but = [(1, 1)]
        for _ in range(q):
            i, j = map(int, stdin.readline().split())
            but.append((i, j))
        but.append((n, m))  
        dp = {}
        ans = solve(0, 0, 0, 0) + 1
        print(ans)
        line = stdin.readline().strip()

main()
