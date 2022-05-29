# 소수 구하기
"""
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
"""


M, N = map(int, input().split())

sosu = [0]*(N+1)
x = int(len(sosu)**0.5)+1

sosu[1] = 1
for i in range(2, x+1):
    if sosu[i] == 0:
        for j in range(i+i, len(sosu), i):
            sosu[j]=1

for i in range(M, len(sosu)):
    if sosu[i] == 0:
        print(i)
