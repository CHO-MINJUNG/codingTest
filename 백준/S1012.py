# 유기농 배추
"""
입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 그 다음 줄부터 각각의 테스트 케이스에 대해 첫째 줄에는 배추를 심은 배추밭의 가로길이 M(1 ≤ M ≤ 50)과 세로길이 N(1 ≤ N ≤ 50), 그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)이 주어진다. 그 다음 K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다. 두 배추의 위치가 같은 경우는 없다.
"""

def ji(i, j):
    if i<0 or j<0 or i>=len(arr) or j>=len(arr[0]):
        return
    if arr[i][j]==1:
        arr[i][j]=0
        ji(i,j-1)
        ji(i-1,j)
        ji(i+1,j)
        ji(i,j+1)
    return

# i -> 세로 j -> 가로
T = int(input())
for i in range(T):
    M, N, K = list(map(int, input().split()))
    arr = [[0]*(M) for _ in range(N)]
    for _ in range(K):
        j, i = list(map(int, input().split()))
        arr[i][j]=1
    sum = 0
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            if arr[x][y]==1:
                sum += 1
                ji(x, y)

    print(sum)





# 찾아본 코드가 메모리, 시간 모두 절반 ㅎ..
"""
from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

t = int(input())

def bfs(graph, a, b):
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >=n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
    return

for i in range(t):
    cnt = 0
    n, m, k = map(int,input().split())
    graph = [[0]*m for _ in range(n)]

    for j in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1:
                bfs(graph, a, b)
                cnt += 1
    print(cnt)
"""