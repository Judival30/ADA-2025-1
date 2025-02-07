from sys import stdin
from sys import setrecursionlimit

setrecursionlimit(10**6)

id, n, m, ansSize = 0, 0, 0, 0
sizebit = 0

bitm = []
tab = [[-1 for j in range(201)] for i in range(201)]


def dfsBtoD(ans : list, i1, i2, j1, j2):
    global bitm, ansSize
    res = 0
    if not (i1 > i2 or j1 > j2) and i1 < n and i2 < n and j1 < m and j2 < m:
        if i1 == i2 and j1 == j2:
            res = tab[i1][j1]
        else:
            cont = 0
            dirt = [-1 for i in range(4)]
            top = 1
            mid_i = (i1 + i2) // 2
            mid_j = (j1 + j2) // 2
            #print("TL")
            dirt[0] = dfsBtoD(ans, i1, mid_i, j1, mid_j)
            if 0 <= i1 < n and 0 <= mid_i < n and 0 <= mid_j + 1 < m  and 0 <= j2 < m:
                #print("TR")
                dirt[1] = dfsBtoD(ans, i1, mid_i, mid_j + 1, j2)
                top += 1
            if 0 <= mid_i + 1 < n and 0 <= i2 < n and 0 <= j1 < m  and 0 <= mid_j < m:
                #print("BL")
                top += 1
                dirt[2] = dfsBtoD(ans, mid_i + 1, i2, j1, mid_j)
            if 0 <= mid_i + 1 < n and 0 <= i2 < n and 0 <= mid_j + 1 < m  and 0 <= j2 < m:
                #print("BR")
                top += 1
                dirt[3] = dfsBtoD(ans, mid_i + 1, i2, mid_j + 1, j2)
          
            for k in dirt:
                if k != -1:
                    cont += k
            if cont == 0:
                ans.append(0)
            elif cont == top:
                res = 1
                ans.append(1)
            else:
                ans.append("D")
                for k in dirt:
                    if k != -1:
                        ans.append(k)

            #print("cont: ", cont, ans)
    return res


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
        fort, n, m = map(int, line.split()) 
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
                    tab[i][j] = int(lb[id])
                    id += 1
            id = 0
            ans1 = []
            dfsBtoD(ans1, 0, n - 1, 0, m - 1)
            cont = 0
       
            for i in range(len(ans1) - 1):
                if cont == 50:
                    cont = 0
                    print()
                cont += 1
                print(ans1[i], end="")
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