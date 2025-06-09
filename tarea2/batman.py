"""
Juan Diego Valencia Alomia
codigo: 8977467
"""
from sys import stdin


class Vil:
    def __init__(self, deff, sp):
        self.deff = deff
        self.spSet = set(sp)
class Sup:
    def __init__(self, name, val, cost):
        self.name = name
        self.val = val
        self.cost = cost
        
spLst, vilLst = [], []
dp = {}
def solve(i, j):
    ans = None
    if j == 0 and i >= 0:
        ans = 0
    elif i == 0:
        ans = float("inf")
    elif (i, j) in dp:
        ans = dp[(i, j)]
    elif spLst[i - 1].name in vilLst[j - 1].spSet and spLst[i - 1].val >= vilLst[j - 1].deff:
        ans = min(spLst[i - 1].cost + solve(i - 1, j - 1), solve(i - 1, j))
    else:
        ans = solve(i - 1, j)
  
    
    dp[(i, j)] = ans
    return ans
    

def main():
    global spLst, vilLst, dp
    p, v, e = map(int, stdin.readline().strip().split())
    cs = 1
    while p != 0 and v != 0 and e != 0:
        spLst = []
        vilLst = []
        for i in range(p):
            name, val, cost = stdin.readline().strip().split()
            spLst.append(Sup(name, int(val), int(cost)))
        for i in range(v):
            name, deff, lst = stdin.readline().strip().split()
            vilLst.append(Vil(int(deff), lst.split(",")))
        dp = {}
        ans = solve(len(spLst), len(vilLst))
    
        if ans > e:
            print("No")
        else:
            print("Yes")
        cs+=1

        p, v, e = map(int, stdin.readline().strip().split())
main()