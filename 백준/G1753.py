# 최단경로
"""
방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오. 단, 모든 간선의 가중치는 10 이하의 자연수이다.
"""
from cmath import inf
import sys

V, E = list(map(int, input().split()))
startV = int(input())
result = [{}]*V
weight = [{}]*V

for i in range(E):
    u, v, w = list(map(int, sys.stdin.readline().strip().split()))
    result[u-1].append({[v-1]:w})
    print(result)
for x in range(V):
    for i in result[x].keys():
        print(x, i)
        for y in range(V):
            if result[i].get(y) is not None:
                if y not in result[x]:
                    print("오긴 오니")
                    result[x][y] = result[x][i]+result[i][y]
                else:
                    result[x][y] = min(result[x][y], result[x][i]+result[i][y])
print(result)

# for i in result[startV-1]:
#     if i==inf:
#         i = "INF"
#     print(i)