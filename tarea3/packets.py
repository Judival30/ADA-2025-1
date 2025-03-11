from sys import stdin
from math import ceil

def solve(box):
    ans = 0
    # 6x6
    ans += box[5]
    # 5x5
    ans += box[4]
    box[0] = max(0, box[0] - 11 * box[4])
    # 4x4
    ans += box[3]
    sp2x2 = 5 * box[3]
    if box[1] < sp2x2:
        box[0] = max(0, box[0] - 4 * (sp2x2 - box[1]))
        box[1] = 0
    else:
        box[1] -= sp2x2

    # 3x3
    ans += ceil(box[2] / 4)
    rem3x3 = box[2] % 4
    if rem3x3:
        sp2x2 = 2 * (4 - rem3x3) - 1
        sp1x1 = 36 - 9 * rem3x3 - 4 * min(sp2x2, box[1])
        box[1] = max(0, box[1] - sp2x2)
        box[0] = max(0, box[0] - sp1x1)
    # 2x2
    ans += ceil(box[1] / 9)
    sp2x2 = box[1] % 9
    if sp2x2:
        box[0] = max(0, box[0] - 4 * (9 - sp2x2))   
    # 1x1
    ans += ceil(box[0] / 36)

    return ans

def main():
    line = stdin.readline().strip()
    while line != "0 0 0 0 0 0":
        box = list(map(int, line.split()))
        print(solve(box))
        line = stdin.readline().strip()

main()