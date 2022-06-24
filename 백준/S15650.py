# N과 M(2)
"""
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
고른 수열은 오름차순이어야 한다.
"""

# def backTrack(N, M, arr):
#     if len(arr) == M:
#         print(' '.join(map(str,arr)))
#         return 
#     for i in range(1, N+1):
#         if len(arr)>0 and arr[-1]>=i:
#             continue
#         if i not in arr:
#             arr.append(i)
#             backTrack(N, M, arr)
#             arr.pop()

# N, M = map(int, input().split())

# backTrack(N, M, [])


n,m = list(map(int,input().split()))
s = []
def dfs(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(start,n+1):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()
dfs(1)