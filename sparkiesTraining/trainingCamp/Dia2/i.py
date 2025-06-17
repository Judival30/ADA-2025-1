from sys import stdin

text = list()
L = 0

def f(w):
    line = 0
    curret = 0
    i = 0
    #print("len", len(text))
    while i < len(text) and line < L:
        curret = 0
        flag = True
        #print(i, len(text), flag)
        while i < len(text) and flag:
            word = text[i]
            #print(curret)
            if curret + len(word) <= w:
                curret += len(word) + 1 
                i += 1
            else:
                flag = False
        line += 1
    return i == len(text)

        
def binarysearch(a, b):
    #print(f(10))
    #return
    l, h = a, b
    ans = float('inf')
    while l <= h:
        md = (l + h) // 2
        if f(md):
            ans = min(md, ans)
            h = md-1
        else:
            l = md+1
    return ans

def main():
    global text, L
    L, N = map(int, stdin.readline().split())
    while L != -1:
        text = stdin.readline().split()
        a, b = 0, 0
        for word in text:
            b += len(word) + 1
        b -= 1

        #print(text, a, b)
        ans = binarysearch(a, b)
        print(ans)
        L, N = map(int, stdin.readline().split())

main()