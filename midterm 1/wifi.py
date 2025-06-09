from sys import stdin
h = []
n, m = 0,0 


def pos(d):
    cont = 1
    lim = 2 * d + h[0]
    ans = True
    if lim >= h[-1]:
        ans = True
    else:
        i = 1
        flag = True
        while i < m and ans and flag:
            if h[i] > lim:
                cont += 1
                lim = 2 * d + h[i]
            if cont > n:
                ans = False
            if lim >= h[-1]:
                flag = False
            i += 1
    return ans


def bisec(l, r):
    while r - l > 0.05:
        mid = (l + r) / 2.0
        if pos(mid):
            r = mid
        else:
            l = mid
    return r

def main():
    global n, m, h
    t = int(stdin.readline().strip())
    for _ in range(t):
        n, m = map(int, stdin.readline().strip().split())
        h = []
        for i in range(m):
            hi = int(stdin.readline().strip())
            h.append(hi)
        h.sort()
        print("%.1f" % bisec(0, (h[-1] - h[0]) / 2.0))

main()

        