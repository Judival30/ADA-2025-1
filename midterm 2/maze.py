from sys import stdin

n, m = 0, 0
mat = []
ways = [(1, 0), (0, -1), (0, 1), (-1, 0)]
ini = (float("inf"),float("inf"))
ext = (float("inf"),float("inf"))


def check(i, j, a, vis):
    ans = True
    if not(0 <= i < n and 0 <= j < m and not vis[i][j]):
        ans = False
    elif mat[i][j] != a:
        ans = False
    return ans


def solve(i, j, a, d, vis):
    global ini, ext
    if i == n - 1:
        if (pi, pj) < ini or ((pi, pj) == ini and (i, j) < ext):
            ini = (pi, pj)
            ext = (i, j)
    else:        
        vis[i][j] = True

        na = a + 1
        nd = d
        if na > d:
            nd = d + 1
            na = 1

        for ix, jx in ways:
            ni = i + ix
            nj = j + jx
            if check(ni, nj, na, vis):
                solve(ni, nj, na, nd, vis)
  
        vis[i][j] = False
 
    
def rd():
    return stdin.readline().strip()


def main():
    global n, m, mat, ini, ext, pi, pj
    t = int(rd())
    for cs in range(t):
        b = rd()
        n, m = map(int, rd().split())
        mat = []
        pos = []
        for i in range(n):
            row = list(map(int, rd().split()))
            if i == 0:
                for j in range(m):
                    if row[j] == 1:
                        pos.append(j)
            mat.append(row)
       
        ini = (float("inf"),float("inf"))
        ext = (float("inf"),float("inf"))


        for j in pos:
            vis = [[False for j in range(m)] for i in range(n)]
            pi, pj = 0, j
            solve(0, j, 1, 1, vis)

        print(ini[0] + 1, ini[1] + 1)
        print(ext[0] + 1, ext[1] + 1)

        if cs < t - 1:
            print()
        


main()
        
