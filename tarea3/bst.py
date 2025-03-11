from sys import stdin
import math


def solve(l, r, h): 
    ans = []
    if l > r:
        ans = []
    elif l == r:
        ans = [l]
    else:
        root =  r - ((1 << (h - 1)) - 1)
        if root < l: 
            ans = [l] + solve(l + 1, r, h - 1)
        else: 
            ans = [root] + solve(l, root - 1, h - 1) + solve(root + 1, r, h - 1)
    return ans


def main():
    n, h = map(int, stdin.readline().strip().split())
    c = 1
    while n != 0 and h != 0:
        if n == 0 or h < math.ceil(math.log2(n + 1)):
            print("Case %d: Impossible." % c)
        else:
            print("Case %d:" % c, end=" ")
            print(*solve(1, n, h))
        n, h = map(int, stdin.readline().strip().split())
        c += 1

main()
