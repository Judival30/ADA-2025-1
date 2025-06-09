"""
Juan Diego Valencia Alomia
codigo: 8977467
"""
from sys import stdin

mat = []
dp = {}
maxSum = []
res = float("inf")

def solve(i, j, acum):
    global mat, dp, maxSum, res
    key = (i, j, acum)
    ans = None 
    if key in dp:
        ans = dp[key]
    elif i == len(mat) - 1 and j == 0:
        ans = abs(acum)
    else: 
        minSum = max(0, abs(acum) - maxSum[i])
        ans = float("inf")
        if minSum < res:
            ways = [j]
            if len(mat[i + 1]) > len(mat[i]):
                ways.append(j + 1)
            else:
                ways.append(j - 1)
            for jx in ways:
                if 0 <= jx < len(mat[i + 1]):
                    w = mat[i + 1][jx]
                    add = solve(i + 1, jx, acum + w)
                    sub = solve(i + 1, jx, acum - w)
                    ans = min(ans, add, sub)
    
    dp[key] = ans  
    res = min(res, ans)  
    return ans 

def main():
    global mat, dp, maxSum, res
    
    n = int(stdin.readline().strip())
    while n != 0:
    
        mat = []
        dp = {}
        maxSum = []
        res = float("inf")
    
        for _ in range(2 * n - 1):
            mat.append(list(map(int, stdin.readline().strip().split())))
        
        maxSum = [50 * (len(mat)- 1 - i) for i in range(len(mat))]
        
        solve(0, 0, mat[0][0])  
        print(res)
        n = int(stdin.readline().strip())


main()