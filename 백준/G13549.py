# 숨바꼭질 3
"""
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.
"""

from collections import deque

N, K = list(map(int, input().split()))
MAX = 200001
result = [0]*MAX
bool_result = [False]*MAX
deq=deque()
deq.append(N)

def isEqual(u, K):
    if u==K:
        result[u]
        print()
        return True
    return False

while deq:
    u = deq.popleft()
    check = False
    bool_result[u]=True
    if bool_result[u-1]==False and check==False:
        result[u-1] = result[u]+1
        check =isEqual(u-1, K)
        deq.append(u-1)
    
    if 0<=u+1<MAX and bool_result[u+1]==False and check==False:
        result[u+1] = result[u]+1
        check =isEqual(u+1, K)
        deq.append(u+1)

    if 0<=2*u < MAX:
        if bool_result[2*u]==False and check==False:
            result[2*u] = result[u]
            check =isEqual(2*u, K)
            deq.append(2*u)
    if check:
        break
