from sys import stdin
import heapq

def solve(lst):
    pq = []
    t = 0
    for q, d in lst:
        t += q
        heapq.heappush(pq, (-q))
        if t > d:
            t -= abs(heapq.heappop(pq)) 
    return len(pq)

def main():
    t = int(stdin.readline().strip())
    for cs in range(t):
        b = stdin.readline()
        n = int(stdin.readline().strip())
        lst = []
        for i in range(n):
            q, d = map(int, stdin.readline().strip().split())
            lst.append((q, d))
        lst.sort(key= lambda x: x[1])
        print(solve(lst))
        if cs < t - 1:
            print()


main()
