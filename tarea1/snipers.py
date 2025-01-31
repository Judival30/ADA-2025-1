from sys import stdin
import math


k, s, f, d = 0, 0, 0, 0
sold = []


def pos(m):
    intv = []
    ans = True
    i = 0
    while i < len(sold) and ans:
        xs, ys = sold[i]
        dy = ys - k + m
        if dy > d:
            ans = False
        else:
            dx = math.sqrt(d * d - dy * dy) 
            #intv.append((math.floor(xs - dx), math.ceil(xs + dx)))
            intv.append((xs - dx, xs + dx))
        i += 1
    if ans:
        intv.sort(key=lambda x: x[1])
        #print(*intv, "m:", m)
        act = -float("inf")
        cont = 0
        i = 0
        while i < len(intv) and ans:
            l, r = intv[i]
            if act < l:
                act = r
                cont += 1
            
            if cont > f:
                ans = False
            i += 1
    return ans


def bisec(l, r):
    if l > r:
        ans = -1
    else:
        mid = (l + r) // 2
        if pos(mid):
            ans = mid
            m = bisec(mid + 1, r)
            if m != -1:
                ans = m
        else:
            ans = bisec(l, mid - 1)
    return ans

def main():
    global k, s, f, d, sold
    n = int(stdin.readline().strip())
    for c in range(1, n + 1):
        b = stdin.readline()
        k, s, f, d = map(int, stdin.readline().strip().split())
        sold = []
        for i in range(s):
            x, y = map(int, stdin.readline().strip().split())
            sold.append((x, y))
        
        m = bisec(0, d)
        if m == -1:
            print("Case %d: IMPOSSIBLE" % (c))
        else:
            print("Case %d: %d" % (c, m))

main()

        

