"""
Juan Diego Valencia Alomia
codigo: 8977467
"""
from sys import stdin

cad = ""
dp = {}


def solve(l, r):
    ans = False
    if l == r and (cad[l] == "T" or cad[l] == "A"):
        ans = True
        #print(cad[l])
    elif l == r:
        ans = False
    elif (l, r) in dp:
        ans = dp[(l, r)]
     
    elif l < r:
        
        if cad[l] == "A" and cad[r] == "C":
            ans = solve(l + 1, r) or solve(r , l + 1) or solve(l, r - 1)
        elif cad[l] == "A" :
            ans = solve(l + 1, r) or solve(r , l + 1)
        elif cad[l] == "G" and cad[r] == "C" and abs(r - l) >= 2:
            ans = solve(r - 1, l + 1) or solve(l, r - 1)
        elif cad[r] == "C":
            ans = solve(l, r - 1)
        
    else:
        if cad[l] == "A" and cad[r] == "C":
            ans = solve(r , l - 1) or solve(l - 1, r) or solve(l, r + 1)
        elif cad[l] == "A":
            ans =  solve(r , l - 1) or solve(l - 1, r)
        elif cad[l] == "G" and cad[r] == "C" and abs(r - l) >= 2:
            ans = solve(r + 1, l - 1) or solve(l, r + 1)
        elif cad[r] == "C":
            ans = solve(l, r + 1)
        
    dp[(l, r)] = ans
    return ans


def main():
    global dp, cad
    line = stdin.readline().strip()
    while line != "":
        n, cad = line.split()
        n = int(n)
        #print(cad)
        if n == 1 and (cad[0] == "A" or cad[0] == "T"):
            print("simple")
        else:
            dp = {}
            ans = solve(0, n - 1)
            if ans:
                print("mutation")
            else:
                print("doomed")
        line = stdin.readline().strip()
    
main()


    

    