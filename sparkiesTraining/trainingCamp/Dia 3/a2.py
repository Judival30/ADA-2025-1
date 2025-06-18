from sys import stdin
from collections import deque

def main():
    n = int(stdin.readline().strip())
    while n != -1:
        dx = list(map(int, stdin.readline().split()))
        dy = list(map(int, stdin.readline().split()))
        w = [0.0 for i in dx]
        w[0] = (dx[1] - dx[0]) / 2
        w[-1] = (dx[-1] - dx[-2]) / 2
        for i in range(1, n - 1):
            w[i] = (dx[i + 1] - dx[i - 1]) / 2
        ans = 0
        w.sort()
        dy.sort()
        for i in range(n):
            ans += dy[i] * w[i]
        print(ans)
        n = int(stdin.readline().strip())
main()