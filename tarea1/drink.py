from sys import stdin


def binS(stores, m, l, r):
    if l >= r:
        ans =  l
    else:
        mid = (l + r) // 2
        if m < stores[mid]:
            ans = binS(stores, m, l, mid)
        else:
            ans = binS(stores, m, mid + 1, r)
    return ans

def main():
    l = stdin.readline().strip()
    while l != "":
        n = int(l)
        stores = list(map(int, stdin.readline().strip().split()))
        stores.sort()
       
        q = int(stdin.readline().strip())
        for _ in range(q):
            m = int(stdin.readline().strip())
            print(binS(stores, m, 0, len(stores)))

        l = stdin.readline().strip()

main()