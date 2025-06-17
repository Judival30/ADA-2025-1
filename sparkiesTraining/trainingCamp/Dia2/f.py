from sys import stdin



def read():
    return stdin.readline().strip()



def main():
    n = int(read())
    lst = list(map(int, read().split()))
    tot = sum(lst)
    mx = max(lst)
    if 0.45 <= mx / tot:
        print(1)
    elif 0.4 <= mx / tot:
        flag = True
        #print(mx / tot)
        cont = 0
        for n in lst:
            if n != mx:
                p = n / tot
                if (mx / tot) - p < 0.10:
                    flag = False
                    break
            else:
                cont += 1

        if flag and cont <= 1:
            print(1)
        else:
            print(2)
    else:
        print(2)

        
    
main()        

