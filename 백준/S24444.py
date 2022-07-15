# 알고리즘 수업 - 너비 우선 탐색 1
"""
오늘도 서준이는 너비 우선 탐색(BFS) 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.

N개의 정점과 M개의 간선으로 구성된 무방향 그래프(undirected graph)가 주어진다. 정점 번호는 1번부터 N번이고 모든 간선의 가중치는 1이다. 정점 R에서 시작하여 너비 우선 탐색으로 노드를 방문할 경우 노드의 방문 순서를 출력하자.

너비 우선 탐색 의사 코드는 다음과 같다. 인접 정점은 오름차순으로 방문한다
"""

import sys
from collections import deque
sys.setrecursionlimit(100000)

N, M, R = list(map(int, input().split()))
arr = [[] for _ in range(N+1)]
result = [0]*(N+1)
result[R]=1
cnt=[2]

for i in range(M):
    u, v = list(map(int, sys.stdin.readline().strip().split()))
    arr[u].append(v)
    arr[v].append(u)

deq=deque()
def iterator(R):
    arr[R].sort()
    deq.append(R)
    while deq:
        u = deq.popleft()
        arr[u].sort()
        for i in arr[u]:
            if result[i] == 0:
                result[i] = cnt[0]
                cnt[0]+=1  
                deq.append(i)
iterator(R)

for i in range(1, len(result)):
    print(result[i])
