from sys import stdin

l, k, t1, t2, h = 0.0, 0.0, 0.0, 0.0, 0.0
lim = 1e-10


def calc(v):
    ans = v * t1 - k * t2 - k* (t1 - l/v)
    return ans

   

def binS(l, r):
    if r - l < lim:
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
    for _ in range(n):
        l, k, t1, t2, h = map(float, stdin.readline().strip().split())
        v = binS(0, 10000)
        nmin = h
        nmax = h
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
