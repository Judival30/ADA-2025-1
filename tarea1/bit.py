"""
Juan Diego Valencia Alomia
uva: 183 Bit Maps

"""


from sys import stdin
from sys import setrecursionlimit

setrecursionlimit(10**6)

id, n, m, ansSize = 0, 0, 0, 0
sizebit = 0

bitm = []
tab = [[-1 for j in range(501)] for i in range(501)]


def BtoD(i1, i2, j1, j2):
    res = []
    if not (i1 > i2 or j1 > j2) and i1 < n and i2 < n and j1 < m and j2 < m:
        if i1 == i2 and j1 == j2:
            res.append(tab[i1][j1])
        else:
            mid_i = (i1 + i2) // 2
            mid_j = (j1 + j2) // 2
            ways = [(i1, mid_i, j1, mid_j), (i1, mid_i, mid_j + 1, j2), (mid_i + 1, i2, j1, mid_j), (mid_i + 1, i2, mid_j + 1, j2)]
            act = ""
            i = 0
            flag = True
            lsts = []
            for x1, x2, y1, y2 in ways:
                lst = BtoD(x1, x2, y1, y2)
                lsts.extend(lst)   
                if i == 0:
                    act = lst[0]
                elif len(lst) > 0:
                    if act != lst[0] or act == "D":
                        flag = False
                i += 1
         
            if flag and act == "1":
                res.append("1")
            elif flag:
                res.append("0")
            else:
                res.append("D")
                res.extend(lsts)

    return res


def DtoB(i1, i2, j1, j2, b):
    global tab, id
    if not (i1 > i2 or j1 > j2) and i1 < n and i2 < n and j1 < m and j2 < m:
        if b[id] == "D":
            id += 1
            mid_i = (i1 + i2) // 2
            mid_j = (j1 + j2) // 2
            DtoB(i1, mid_i, j1, mid_j, b)
            DtoB(i1, mid_i, mid_j + 1, j2, b)
            DtoB(mid_i + 1, i2, j1, mid_j, b)
            DtoB(mid_i + 1, i2, mid_j + 1, j2, b)
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
        while flag:
            line = stdin.readline().strip()
            tmp = line.split()
            if len(tmp) == 3 or tmp[0] == "#":
                flag = False
            else:
                lines.append(line)
        lb = "".join(lines)
        if fort == "B":
            print("D%4d%4d" % (n, m))
            id = 0
            for i in range(n):
                for j in range(m):
                    tab[i][j] = lb[id]
                    id += 1
            id = 0
            ans1 = BtoD(0, n - 1, 0, m - 1)
            cont = 0
       
            for i in range(len(ans1)):
                if cont == 50:
                    cont = 0
                    print()
                cont += 1
                print(ans1[i], end="")
            print()
        elif fort == "D":
            print("B%4d%4d" % (n, m))
            id = 0
            DtoB(0, n - 1, 0, m - 1, lb)
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