from sys import stdin
from sys import setrecursionlimit

l, k, t1, t2, h = 0.0, 0.0, 0.0, 0.0, 0.0
lim = 1e-10
setrecursionlimit(10**6)

def calc(v):
    ans = v * t1 - k * (t2 + (t1 - l/v))
    return ans

   

def binS(l, r):
    if r - l < 1e-10:
        ans =  l
    else:
        mid = (l + r) / 2
        x =  calc(mid) 
        if h - x < 0:
            ans = binS(l, mid)
        else:
            ans = binS(mid, r)
    return ans



def main():
    global l, k, t1, t2, h, dk
    n = int(stdin.readline().strip())
    nmin = 0
    nmax = 0
    for _ in range(n):
        l, k, t1, t2, h = map(float, stdin.readline().strip().split())
        v = binS(0, 80000)
        if h < l:
            nmin = h
            nmax = h
        elif abs(h - calc(v)) < 1e-7:
            nmax = v * t1
        if h > l:
            nmin = nmax
       
        #print("---", v)
        print("%.6f %.6f" % (nmin, nmax))

main()