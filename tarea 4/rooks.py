"""
Juan Diego Valencia Alomia
Codigo: 8977467
"""

from sys import stdin

ans = float("inf")
mat = []
    
def solve(i, r, vr, vc):
    global ans
    if i == 15:
        j = 0
        pos = r
        while j < 15 and pos >= 0:
            if vc[j]:
                pos -= 1
            j += 1
        if pos >= 0:
            ans = min(ans, r)
    elif r < ans:
        if vr[i]:
            vr[i] = 0
            tmp = []
            for k in range(15):
                if mat[i][k] == "#":
                    tmp.append((k, vc[k]))
                    vc[k] = max(0, vc[k] - 1)   
            solve(i + 1, r + 1, vr, vc)
            for k, val in tmp:
                vc[k] = val
            vr[i] = 1
        solve(i + 1, r, vr, vc)

def main():
    global ans, mat
    line = stdin.readline().strip()
    while line != "END":
        mat = []
        
        vc = [0 for i in range(15)]
        vr = [0 for i in range(15)]

        for i in range(15):
            if line != "END":
                for j in range(15):
                    if line[j] == "#":       
                        vr[i] += 1
                        vc[j] += 1
                mat.append(list(line))
            line = stdin.readline().strip()    
       
        ans = float("inf")
        solve(0, 0, vr, vc)
        
        print(ans)
main()