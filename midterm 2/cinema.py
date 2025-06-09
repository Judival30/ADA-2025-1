"""
Juan Diego Valencia Alomia
Codigo: 8977467
"""

from sys import stdin


def solve(p, mat):
    ans = True
    k = 0
   
    while k < len(p) and ans:
        i, j = p[k]
        if mat[i][j] and mat[i][j + 1]:
            ans = False
        elif not mat[i][j]:
            mat[i][j] = True
        elif not mat[i][j + 1]:
            mat[i][j + 1] = True
        k += 1
    return ans

    
def rd():
    return stdin.readline().strip()

def main():
    n, m = map(int, rd().split())
    while n != 0 and m != 0:
        p = int(rd())
        mat = [[False for j in range(m + 1)] for i in range(n)]
        for _ in range(p):
            pos, dir = map(str, rd().split())
            i = ord(pos[0]) - 65
            j = int(pos[1:]) - 1
            if dir == "-": 
                mat[i][j] = True
            else:
                mat[i][j + 1] = True
        q = int(rd())
        p = []
        for _ in range(q):
            pos = rd()
            i = ord(pos[0]) - 65
            j = int(pos[1:]) - 1
            p.append((i, j))
        
        p.sort()
        if solve(p, mat):
            print("YES")
        else:
            print("NO")
        n, m = map(int, rd().split())

main()