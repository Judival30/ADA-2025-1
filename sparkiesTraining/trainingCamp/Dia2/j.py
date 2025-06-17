from sys import stdin



def read():
    return stdin.readline().strip()



def main():
    n = int(read())
    while n != -1:
        lst = []
        for _ in range(n):
            k = int(read())
            lst.append(k)
        s = sum(lst)
        
        if s % n == 0:
            ans = 0
            obt = s // n
            disp = 0
            for n in lst:
                if n >= obt:
                    ans += n - obt
            print(ans)
        else:
            print(-1)

            
        n = int(read())
    
main()        

