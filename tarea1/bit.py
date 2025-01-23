from sys import stdin
from sys import setrecursionlimit

setrecursionlimit(10**6)

id, n, m = 0, 0, 0
ans = ""
bitm = ""
tab = [["" for j in range(202)] for i in range(202)]


def dfsBtoD(i1, i2, j1, j2):
    global ans  
    if not (i1 > i2 or j1 > j2) and i1 < n and i2 < n and j1 < m and j2 < m:
        flag = True
        i = i1
        act = tab[i1][j1]
        while i <= i2 and flag:
            j = j1
            while j <= j2 and flag:
                if act != tab[i][j]:
                    flag = False
                j += 1
            i += 1
    
        if flag:
            ans += act
        else:
            ans += "D"
            mid_i = (i1 + i2) // 2
            mid_j = (j1 + j2) // 2
            dfsBtoD(i1, mid_i, j1, mid_j)
            dfsBtoD(i1, mid_i, mid_j + 1, j2)
            dfsBtoD(mid_i + 1, i2, j1, mid_j)
            dfsBtoD(mid_i + 1, i2, mid_j + 1, j2)
    

def dfsDtoB(i1, i2, j1, j2, b):
    global tab, id, bitm
    if not (i1 > i2 or j1 > j2) and i1 < n and i2 < n and j1 < m and j2 < m :
        if b[id] == "D":
            id += 1
            mid_i = (i1 + i2) // 2
            mid_j = (j1 + j2) // 2
            dfsDtoB(i1, mid_i, j1, mid_j, b)
            dfsDtoB(i1, mid_i, mid_j + 1, j2, b)
            dfsDtoB(mid_i + 1, i2, j1, mid_j, b)
            dfsDtoB(mid_i + 1, i2, mid_j + 1, j2, b)
        else:
            
            i = i1
            while i <= i2:
                j = j1
                while j <= j2:
                    tab[i][j] = b[id]
                    j += 1
                i += 1
            id += 1



def main():
    global ans, id, tab, n, m
    line = stdin.readline().strip()
    while line != "#":
        fort, n, m = map(str, line.split())
        n = int(n)
        m = int(m)

        bitm = ""
        if fort == "B":
            ans = ""
            while len(bitm) < n * m:
                line = stdin.readline().strip()
                bitm += line
            
            print("D%4d%4d" % (n, m))
            id = 0
            for i in range(n):
                for j in range(m):
                    tab[i][j] = bitm[id]
                    id += 1
            id = 0
            dfsBtoD(0, n - 1, 0, m - 1)
            cont = 0
            for i in range(len(ans)):
                if cont == 50:
                    cont = 0
                    print()
                cont += 1
                print(ans[i], end="")
            print()
    
        else:
            bitm = stdin.readline().strip()
            print("B%4d%4d" % (n, m))
            id = 0
    
            dfsDtoB(0, n - 1, 0, m - 1, bitm)
            cont = 0
            for i in range(n):
                for j in range(m):
                    if cont == 50:
                        cont = 0
                        print()
                    print(tab[i][j], end="")
                    cont += 1
            print()

        line = stdin.readline().strip()



main()