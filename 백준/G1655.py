# 가운데를 말해요
"""
백준이는 동생에게 "가운데를 말해요" 게임을 가르쳐주고 있다. 백준이가 정수를 하나씩 외칠때마다 동생은 지금까지 백준이가 말한 수 중에서 중간값을 말해야 한다. 만약, 그동안 백준이가 외친 수의 개수가 짝수개라면 중간에 있는 두 수 중에서 작은 수를 말해야 한다.

예를 들어 백준이가 동생에게 1, 5, 2, 10, -99, 7, 5를 순서대로 외쳤다고 하면, 동생은 1, 1, 2, 2, 2, 2, 5를 차례대로 말해야 한다. 백준이가 외치는 수가 주어졌을 때, 동생이 말해야 하는 수를 구하는 프로그램을 작성하시오.
"""
import sys
import heapq

N = int(input())
small = []
big = []

heapq.heapify(small)
heapq.heapify(big)

for i in range(N):
    num = int(sys.stdin.readline())
    if small==[]:
        heapq.heappush(small, -num)
    elif big == []:
        if -small[0] > num:
            heapq.heappush(big, -heapq.heappop(small))
            heapq.heappush(small, -num)
        else:
            heapq.heappush(big, num)
    else:
        if big[0] >= num:
            heapq.heappush(small, -num)
        else:
            heapq.heappush(big, num)
    if len(small)>len(big) and len(small)-len(big)>1:
        heapq.heappush(big, -heapq.heappop(small))
    elif len(big)>len(small):
        heapq.heappush(small, heapq.heappop(big))
    print(-small[0])







# from collections import deque
# import sys

# N = int(input())
# deqleft = deque()
# deqright = deque()
# # print(deqleft[0])

# for i in range(N):
#     num = int(sys.stdin.readline())
#     if len(deqright)==0:
#         if len(deqleft)==0:
#             deqleft.append(num)
#         else:
#             if deqleft[0]>num:
#                 deqleft.appendleft(num)
#             else :
#                 deqright.append(num)
#     elif deqleft[-1] <= num and deqright[0]>=num:
#         deqleft.append(num)
#     elif deqleft[-1]>num:
#         deqleft.appendleft(num)
#     elif deqright[0]<num:
#         deqright.append(num)
#     if len(deqleft)-1>len(deqright):
#         deqright.appendleft(deqleft.pop())
#         deqleft.sort()
#     elif len(deqleft)<len(deqright):
#         deqleft.append(deqright.popleft())    
#         deqright.sort()        
#     print(deqleft[-1])
