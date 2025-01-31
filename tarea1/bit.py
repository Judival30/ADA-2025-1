from sys import stdin
from sys import setrecursionlimit

setrecursionlimit(10**6)

id, n, m, ansSize = 0, 0, 0, 0
sizebit = 0

bitm = []
tab = [["" for j in range(201)] for i in range(201)]


def dfsBtoD(i1, i2, j1, j2):
    global bitm, ansSize
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
            bitm.append(act) 
            ansSize += 1
        else:
            bitm.append("D")  
            ansSize += 1
            mid_i = (i1 + i2) // 2
            mid_j = (j1 + j2) // 2
            dfsBtoD(i1, mid_i, j1, mid_j)
            dfsBtoD(i1, mid_i, mid_j + 1, j2)
            dfsBtoD(mid_i + 1, i2, j1, mid_j)
            dfsBtoD(mid_i + 1, i2, mid_j + 1, j2)


def dfsDtoB(i1, i2, j1, j2, b):
    global tab, id
    if not (i1 > i2 or j1 > j2) and i1 < n and i2 < n and j1 < m and j2 < m:
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



def main1():
    global ansSize, id, tab, n, m, bitm, sizeBit
    line = stdin.readline().strip()
    while line != "#":
        fort, n, m = line.split()
        n, m = int(n), int(m) 
        flag = True
        sizeBit = 0
        lines = []
        bitm = []
        #print("i--------")
        while flag:
            line = stdin.readline().strip()
            tmp = line.split()
            if len(tmp) == 3 or tmp[0] == "#":
                flag = False
            else:
                lines.append(line)
            #print("f--------")
        lb = "".join(lines)
        if fort == "B":
            print("D%4d%4d" % (n, m))
            id = 0
            for i in range(n):
                for j in range(m):
                    tab[i][j] = lb[id]
                    id += 1
            id = 0
            dfsBtoD(0, n - 1, 0, m - 1)
            cont = 0
            for i in range(len(bitm)):
                if cont == 50:
                    cont = 0
                    print()
                cont += 1
                print(bitm[i], end="")
            print()
        elif fort == "D":
            #print(lineD, lines) 
            print("B%4d%4d" % (n, m))
            id = 0
            dfsDtoB(0, n - 1, 0, m - 1, lb)
            cont = 0
            for i in range(n):
                for j in range(m):
                    if cont == 50:
                        cont = 0
                        print()
                    print(tab[i][j], end="")
                    cont += 1
            print()

main1()