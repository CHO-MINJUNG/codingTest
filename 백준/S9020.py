# 골드바흐의 추측
"""
1보다 큰 자연수 중에서  1과 자기 자신을 제외한 약수가 없는 자연수를 소수라고 한다. 예를 들어, 5는 1과 5를 제외한 약수가 없기 때문에 소수이다. 하지만, 6은 6 = 2 × 3 이기 때문에 소수가 아니다.

골드바흐의 추측은 유명한 정수론의 미해결 문제로, 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것이다. 이러한 수를 골드바흐 수라고 한다. 또, 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라고 한다. 예를 들면, 4 = 2 + 2, 6 = 3 + 3, 8 = 3 + 5, 10 = 5 + 5, 12 = 5 + 7, 14 = 3 + 11, 14 = 7 + 7이다. 10000보다 작거나 같은 모든 짝수 n에 대한 골드바흐 파티션은 존재한다.

2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력하는 프로그램을 작성하시오. 만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.
"""

""" 시간이 너무 오래 소요됨!!! 다시 풀어보기"""

# import math

# def sosuBool(num):
#     for z in range(2,(num)):
#         if num%z ==0:
#             return False
#     return True

# cnt = int(input())
# for i in range(cnt):
#     num = int(input())
#     for j in range(num//2,1,-1):
#         sosu = sosuBool(j)
#         if sosu == True:
#             revSosu = sosuBool(num-j)
#             if revSosu == True:
#                 print(j, num-j)
#                 break



"""
에라토스테네스의 체로 다시 품
"""

sosu = [0]*10001
x = int(len(sosu)**0.5)+1

sosu[1] = 1
for i in range(2, x+1):
    if sosu[i] == 0:
        for j in range(i+i, len(sosu), i):
            sosu[j]=1


# sieve = [i for i in range(2, len(sosu)) if sosu[i] == 0]

cnt = int(input())
for i in range(cnt):
    num = int(input())
    for j in range(num//2,1,-1):
        if sosu[j] == 0 and sosu[num-j] == 0:
            print(j, num-j)
            break