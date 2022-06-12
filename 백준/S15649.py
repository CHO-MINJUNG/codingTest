# N과 M (1)
"""
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
"""
def fact(num):
    if num == 1:
        return 1
    return num * fact(num-1)


N, M = map(int, input().split())
num = fact(M-1)

arr = [[0]*M for i in range(num*M)]
for i in range(M):
    for j in range(M):
        for k in range(fact(i)*M):
            arr[k]
print(arr)
