# 스타트와 링크
"""
최대 10C5는 252개의 경우의 수
"""

import time

cnt = int(input())
start_time = time.perf_counter()
arr = [0]*cnt
result = []
for i in range(cnt):
    arr[i] = list(map(int, input().split()))
    for j in range(i):
        arr[j][i] += arr[i][j]
        arr[i][j] = arr[j][i]
print(arr)

 

 

end_time = time.perf_counter()
print(f"time elapsed : {int(round((end_time - start_time) * 1000))}ms")