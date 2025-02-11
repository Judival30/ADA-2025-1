from sys import stdin

L, S = -1, -1
dp = [[[-1 for k in range(27)] for j in range(352)] for i in range(27)]

def precomp(total, used, prev):
    global dp
    if total == 0 and used == 0:
        ans = 1
    elif total <= 0 or used <= 0:
        ans = 0
    elif dp[total][used][prev] != -1:
        ans = dp[total][used][prev]
    else:
        ans = 0
        for i in range(prev + 1, 27):
            if used - i >= 0:
                ans += precomp(total - 1, used - i, i)
        dp[total][used][prev] = ans
    return ans

def main():
    global L, S, dp
    cs = 1
    for total in range(27):
        for used in range(352):  
            precomp(total, used, 0)
    L, S = map(int, stdin.readline().strip().split())
    while L != 0 and S != 0:
        if L > 26 or S < (L * (L + 1)) // 2 or S > (L * (53 - L))// 2 :
            print("Case %d: 0" % cs)
        else:
            print("Case %d: %d" % (cs, precomp(L, S, 0)))
        cs += 1
        L, S = map(int, stdin.readline().strip().split())

main()
