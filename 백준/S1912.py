# 연속합
"""
n개의 정수로 이루어진 임의의 수열이 주어진다. 우리는 이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합을 구하려고 한다. 단, 수는 한 개 이상 선택해야 한다.

예를 들어서 10, -4, 3, 1, 5, 6, -35, 12, 21, -1 이라는 수열이 주어졌다고 하자. 여기서 정답은 12+21인 33이 정답이 된다.
"""

cnt = int(input())
max = -1000
arr = list(map(int, input().split()))
before = -1000
for i in range( len(arr)):
    add = before+arr[i]
    if add>=arr[i]:
        before = add
    else:
        before = arr[i]        
    if max<before:
        max = before
print(max)