from sys import stdin

lim = 1e-10


def solve(x, l, r):
    if r - l < lim:
        ans = True
    else:
        mid1 = l + (r - l) / 3  
        mid2 = r - (r - l) / 3 
        if mid1 <= x <= mid2:
            ans = False
        elif x < mid1:  
            ans = solve(x, l, mid1)
        else:
            ans = solve(x, mid2, r)
    return ans
   

def main():
    l = stdin.readline().strip()
    while l != "END":
        x = float(l)
        if solve(x, 0, 1):
            print("MEMBER")
        else:
            print("NON-MEMBER")
        l = stdin.readline().strip()

main()

