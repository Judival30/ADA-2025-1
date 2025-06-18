from sys import stdin


def main():
    n, k = map(int, stdin.readline().strip().split())

    lst = list(map(int, stdin.readline().split()))
    cont = [0 for i in lst]
    used = [False for i in lst]
    flag = True
    i = 0
    ans = 0
    while flag:
        if i == len(lst):
            i = 0
        if lst[i] >= k and cont[i] < 3:
            lst[i] -= k
            cont[i] += 1
        elif (cont[i] == 3 or lst[i] < k) and not used[i]:
            used[i] = True
        else:
            flag = False
        i +=1
    
    print(sum(lst))

main()
