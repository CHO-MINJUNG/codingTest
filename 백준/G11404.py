# 플로이드
"""
n(2 ≤ n ≤ 100)개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 m(1 ≤ m ≤ 100,000)개의 버스가 있다. 각 버스는 한 번 사용할 때 필요한 비용이 있다.

모든 도시의 쌍 (A, B)에 대해서 도시 A에서 B로 가는데 필요한 비용의 최솟값을 구하는 프로그램을 작성하시오.
"""
from cmath import inf
import sys

dosi = int(input())
bus = int(input())
result = [[inf]*dosi for _ in range(dosi)]
for i in range(bus):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    result[a-1][b-1]=min(result[a-1][b-1], c)
for i in range(dosi):
    result[i][i]=0
for i in range(dosi):
    for x in range(dosi):
        for y in range(dosi):
            if x==y:
                continue
            if result[x][i]+result[i][y]<result[x][y]:
                result[x][y]=result[x][i]+result[i][y]

for i in result:
    print(' '.join(map(str,i)))