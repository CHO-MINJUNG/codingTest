# 계단 오르기
"""
입력의 첫째 줄에 계단의 개수가 주어진다.

둘째 줄부터 한 줄에 하나씩 제일 아래에 놓인 계단부터 순서대로 각 계단에 쓰여 있는 점수가 주어진다. 계단의 개수는 300이하의 자연수이고, 계단에 쓰여 있는 점수는 10,000이하의 자연수이다.
"""

cnt = int(input())
arr = [0]*cnt
for i in range(cnt):
    arr[cnt-i-1] = int(input())

result = [[0]*(cnt) for _ in range(2)]

if cnt>2:
    result[0][0], result[1][0] = arr[0], arr[0]
    result[0][1] = arr[0]+arr[1]
    result[1][2] = arr[0]+arr[2]
    for i in range(3, cnt):
        result[0][i] = arr[i]+result[1][i-1]
        result[1][i] = arr[i]+max(result[0][i-2], result[1][i-2])
    print(max(map(max, result)))
else:
    print(sum(arr))
print(result)