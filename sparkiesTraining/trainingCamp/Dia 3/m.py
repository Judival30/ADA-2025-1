from sys import stdin


def main():
    n = int(stdin.readline().strip())
    while n:
        lst = list(map(int, stdin.readline().split()))
        lst.sort(reverse=True)
        ans = 0
        for h in range(n):            
            if h + 1 <= lst[h]:
                ans = h + 1
            else:
                break
        print(ans)
        n = int(stdin.readline().strip())

main()