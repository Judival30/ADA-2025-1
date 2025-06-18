from sys import stdin
from collections import deque

def main():
    n = int(stdin.readline().strip())
    while n != -1:
        dx = list(map(int, stdin.readline().split()))
        dyi = list(map(int, stdin.readline().split()))
     
        dyi.sort(reverse=True)
        dy = deque()
        for i in range(n):
            if i % 2 != 0:
                dy.append(dyi[i])
            else:
                dy.appendleft(dyi[i])

        
        ans = 0
        print(dx, dy)
        for i in range(1, n):
            #print(dx[i - 1], dy[i - 1] ,"|", dx[i], dy[i])
            if dy[i - 1] > dy[i]:
                #print("sup", ((dx[i] - dx[i - 1]) * (dy[i - 1] - dy[i])) / 2, dy[i] * (dx[i] - dx[i - 1]))
                ans += ((dx[i] - dx[i - 1]) * (dy[i - 1] - dy[i])) / 2#Triangulo
                ans += dy[i] * (dx[i] - dx[i - 1])
            elif dy[i - 1] < dy[i]:
                #print("in", ((dx[i] - dx[i - 1]) * (dy[i] - dy[i -1])) / 2, dy[i - 1] * (dx[i] - dx[i - 1]))
                ans += ((dx[i] - dx[i - 1]) * (dy[i] - dy[i -1])) / 2#Triangulo
                ans += dy[i - 1] * (dx[i] - dx[i - 1])
            else:
                #print("cuad", dy[i - 1] * (dx[i] - dx[i - 1]))
                ans += dy[i - 1] * (dx[i] - dx[i - 1])
        
        print(ans)
        #print("//////////////")
        n = int(stdin.readline().strip())

main()