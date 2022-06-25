# 계단 오르기
"""
입력의 첫째 줄에 계단의 개수가 주어진다.

둘째 줄부터 한 줄에 하나씩 제일 아래에 놓인 계단부터 순서대로 각 계단에 쓰여 있는 점수가 주어진다. 계단의 개수는 300이하의 자연수이고, 계단에 쓰여 있는 점수는 10,000이하의 자연수이다.
"""

cnt = int(input())
arr = [0]*cnt
for i in range(cnt):
    arr[cnt-i-1] = int(input())

result = arr[0]
idx = 1
while True:
    if idx>len(arr)-1 :
        break
    if idx == len(arr)-1:
        result += arr[idx]
        break
    if arr[idx] > arr[idx+1]:
        result += arr[idx]
        idx +=2
    else:
        result+= arr[idx+1]
        idx+=2

print(result)