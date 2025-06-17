from sys import stdin



def read():
    return stdin.readline().strip()



def main():
    t = int(read())
    ans = []
    i = 1
    while len(ans) < 1001:
        if not ("3" in str(i)[-1] or i % 3 == 0):
            ans.append(i)
        i += 1
    for _ in range(t):
        n = int(read())
        print(ans[n - 1])
main()        

