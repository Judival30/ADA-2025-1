from sys import stdin

def main():
    inf = open("input.txt", "r")
    contend = inf.read().split()
    
    n, k = int(contend[0]), int(contend[1])
    lst = list(map(int, contend[2:]))
    for i in range(n):
        j = 0
        while lst[i] >= k and j < 3:
            lst[i] -= k
            j += 1
    outf = open("output.txt","w")
    print(sum(lst),file=outf)


main()
