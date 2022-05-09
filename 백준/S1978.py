# 소수 찾기
"""
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
"""

cnt = int(input())
num_list = list(map(int, input().split()))

for i in num_list:
    if i==1:
        cnt-=1
    for j in range(2,i):
        if i%j ==0:
            cnt-=1
            break
print(cnt)