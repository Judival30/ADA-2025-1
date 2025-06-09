"""
Juan Diego Valencia Alomia
codigo: 8977467
"""

from sys import stdin

dp = {}
mega, robGuns = [], []
n = 0

def solve(mask):
    if mask == (1 << n) - 1:
        ans = 1
    elif mask in dp:
        ans = dp[mask]
    else:
        ans = 0     
        for j in range(n):
            if not (mask & 1 << j) and (mega[j] or (mask & robGuns[j])):
                ans += solve(mask | (1 << j))
        dp[mask] = ans
    return ans



def main():
    global mega, robGuns, dp, n
    t = int(stdin.readline().strip())
    for cs in range(1, t + 1):
        n = int(stdin.readline().strip())
        mega = [0 for i in range(n)]
        robGuns = [0 for i in range(n)]
        mat = []
        for i in range(n + 1):
            line = stdin.readline().strip()
            mat.append(line)
        
        for i in range(n):
            if mat[0][i] == "1":
                mega[i] = 1
        for j in range(n):
            mask = 0
            for i in range(1, n + 1):
                if mat[i][j] == "1":
                    mask |= (1 << i - 1)
            robGuns[j] = mask
       
        dp = {}
        print("Case %d: %d" % (cs, solve(0)))
    
main()