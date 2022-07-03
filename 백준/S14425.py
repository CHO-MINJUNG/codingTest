# 문자열 집합
"""
총 N개의 문자열로 이루어진 집합 S가 주어진다.

입력으로 주어지는 M개의 문자열 중에서 집합 S에 포함되어 있는 것이 총 몇 개인지 구하는 프로그램을 작성하시오.
"""
import sys

N, M = map(int, input().split())

Nset= set()
cnt = 0
for i in range(N):
    Nset.add(sys.stdin.readline())
for i in range(M):
    if sys.stdin.readline() in Nset:
        cnt+=1
        

print(cnt)

"""
s= set([input() for _ in range(N)])
을 사용해서 한 줄로 표현한 것이 신기해서..
"""