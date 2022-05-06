# 링
"""
링의 반지름이 주어진다. 이때, 첫 번째 링을 한 바퀴 돌리면, 나머지 링은 몇 바퀴 돌아가는지 구하는 프로그램을 작성하시오.
"""

def GCD(abList):
    maxNum = max(abList)
    minNum = min(abList)
    return minNum, maxNum%minNum 

N = int(input())

numList =  list(map(int, input().split()))
FIRSTNUM = numList[0]

for i in range(1, N):
    a, b = FIRSTNUM , numList[i]
    gong= 1
    while True:
        if a==0 or b==0:

            gong = max([a,b])
            break
        a, b = GCD([a,b])
    print(str(FIRSTNUM//gong)+"/"+str(numList[i]//gong))
    