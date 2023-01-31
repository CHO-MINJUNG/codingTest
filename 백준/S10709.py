## https://www.acmicpc.net/problem/10709

import sys

H, W = map(int, sys.stdin.readline().split())
for i in range(H):
    l = list(sys.stdin.readline().strip())
    cnt = -1
    for j in l:
        if j=='.': 
            if cnt!=-1:
                cnt+=1
        else:
            cnt = 0
        print(cnt, end=" ")
    print()