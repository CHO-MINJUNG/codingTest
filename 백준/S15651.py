# N과 M(3)
"""
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.
"""

n,m = list(map(int,input().split()))
arr = []

def backTrack(start):
    if len(arr) == m:
        print(' '.join(map(str,arr)))
        return
    for i in range(start, n+1):
        arr.append(i)
        backTrack(start)
        arr.pop()

backTrack(1)