from sys import stdin

def main():
    t = int(stdin.readline().strip())
    while t != 0:
        n = int(stdin.readline().strip())
        S, d = 0, 1
        while(S < n):
            S += d
            d += 1
        diag = d - 1
        S = S - diag
        rest = n - S

        a = diag - rest + 1
        b = diag + 1 - a
    
        if diag % 2 == 0:
            a, b = b, a
        

        print("TERM %d IS %d/%d" %(n, a, b))
        t -= 1

main()


