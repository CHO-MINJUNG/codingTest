# 쿼드트리
"""
첫째 줄에는 영상의 크기를 나타내는 숫자 N 이 주어진다. N 은 언제나 2의 제곱수로 주어지며, 1 ≤ N ≤ 64의 범위를 가진다. 두 번째 줄부터는 길이 N의 문자열이 N개 들어온다. 각 문자열은 0 또는 1의 숫자로 이루어져 있으며, 영상의 각 점들을 나타낸다.
"""

N = int(input())

arr = []*N
result = []
for i in range(N):
    arr.append(list(input()))

def quad(n, x, y, plus):
    sample = arr[x][y]
    if plus == "(":
        result.append(plus)
    for i in range(x, x+n):
        for j in range(y, y+n):
            if sample != arr[i][j]:
                quad(n//2, x, y, "(")
                quad(n//2, x, y+n//2, "")
                quad(n//2, x+n//2, y, "")
                quad(n//2, x+n//2, y+n//2, "")
                result.append(")")
                return
    result.append(sample)

quad(N, 0, 0, "")
print(''.join(map(str,result)))