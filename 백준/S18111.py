# 마인크래프트
"""
첫째 줄에 N, M, B가 주어진다. (1 ≤ M, N ≤ 500, 0 ≤ B ≤ 6.4 × 107)

둘째 줄부터 N개의 줄에 각각 M개의 정수로 땅의 높이가 주어진다. (i + 2)번째 줄의 (j + 1)번째 수는 좌표 (i, j)에서의 땅의 높이를 나타낸다. 땅의 높이는 256보다 작거나 같은 자연수 또는 0이다.
"""

N, M, B = list(map(int, input().split(" ")))
arr = []*N
for i in range(N):
    arr.append(list(map(int, input().split(" "))))

time = 0
height = 0
maxCnt = max(map(max,arr))
minCnt = min(map(min,arr))

for i in range(minCnt, maxCnt+1):
    now = 0
    inven = B
    for j in arr:
        for z in range(len(j)):
            if i>j[z]:
                now+=i-j[z]
                inven-=i-j[z]
            elif i<j[z]:
                now+=(j[z]-i)*2
                inven+=j[z]-i
    if inven >=0:
        if time>=now or time ==0:
            time = now
            height = i
            
print(time, height)

