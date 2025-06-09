from sys import stdin

ans = 0

def check(r, c, p, T):
    ans = True
    i = 0
    aux = T[r][c] 
    T[r][c] = 0
    while i < 9 and ans:
        if T[i][c] == p or T[r][i] == p:
            ans = False
        i += 1
    rr, cc = (r // 3) * 3, (c // 3) * 3
    i = rr
    while i < rr + 3 and ans:
        j = cc
        while j < cc + 3 and ans:
            if T[i][j] == p:
                ans = False
            j += 1
        i += 1
    T[r][c] = aux
    return ans

def backSudoku(r, c, T):
    global ans
    if ans < 2 and ans != -1:
        if r == 9:
            ans += 1
        else:
            if c == 9:
                backSudoku(r + 1, 0, T)
            else:
                if T[r][c] != 0:
                    if check(r, c, T[r][c], T):
                        backSudoku(r, c + 1, T)
                    else:
                        ans = -1
                else:
                    for v in range(1, 10):
                        if check(r, c, v, T):
                            T[r][c] = v
                            backSudoku(r, c + 1, T)
                    T[r][c] = 0


def main():
    global ans
    line = list(map(int, stdin.readline().strip().split()))
    c = 1
    while len(line) != 0:
        mat = [line]
        ans = 0
        for _ in range(8):
            line = list(map(int, stdin.readline().strip().split()))
            mat.append(line)
        flag = True
        i = 0
        cont = 0
        while i < 9 and flag:
            j = 0
            while j < 9 and flag:
                if mat[i][j] != 0 and not check(i, j, mat[i][j], mat):
                    ans = -1
                    flag = False
                if mat[i][j] != 0:
                    cont += 1
                   
                j += 1
            i += 1
       
        if ans == 0:
            backSudoku(0, 0, mat)
        if ans == 0:
            print("Case %d: Impossible." % c)
        elif ans == -1:
            print("Case %d: Illegal." % c)
        elif ans == 2:
            print("Case %d: Ambiguous." % c)
            #print(cont)
        elif ans == 1:
            print("Case %d: Unique." % c)
            #print(cont)
     
        
        b = stdin.readline()
        line = list(map(int, stdin.readline().strip().split()))
        c += 1
main()

