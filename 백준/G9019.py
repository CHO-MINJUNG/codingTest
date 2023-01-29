# acmicpc.net/problem/9019
from collections import deque


cnt = int(input())
for i in range(cnt):
    a, b = map(int, input().split())
    testCase = deque()
    testCase.append([a,''])
    visited = [0]*10001
    while True:
        now = testCase.popleft()
        nowNum = now[0]
        nowResult = now[1]

        if nowNum == b:
            print(nowResult)
            break

        
        if nowNum*2>9999:
            double = (nowNum*2)%10000
        else:
            double =  nowNum*2
        if visited[double] == 0:
            testCase.append([double, nowResult+'D'])
            visited[double] = 1

        if nowNum == 0:
            subt=9999
        else:
            subt=nowNum-1

        if visited[subt]==0:
            testCase.append([subt, nowResult+'S'])
            visited[subt]=1

        c = nowNum%1000
        d = nowNum//1000
        left = c*10 + d
        if visited[left]==0:
            testCase.append([left, nowResult+'L'])
            visited[left]=1
        
        c = nowNum%10
        d = nowNum//10
        right = c*1000 + d
        if visited[right]==0:
            testCase.append([right, nowResult+'R'])
            visited[right]=1