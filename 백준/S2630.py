# 색종이 만들기
"""
첫째 줄에는 전체 종이의 한 변의 길이 N이 주어져 있다. N은 2, 4, 8, 16, 32, 64, 128 중 하나이다. 색종이의 각 가로줄의 정사각형칸들의 색이 윗줄부터 차례로 둘째 줄부터 마지막 줄까지 주어진다. 하얀색으로 칠해진 칸은 0, 파란색으로 칠해진 칸은 1로 주어지며, 각 숫자 사이에는 빈칸이 하나씩 있다.
"""

N = int(input())

arr = []*N
white = []
blue = []
for i in range(N):
    arr.append(input().split())

def paper(n, x, y):
    sample = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if sample != arr[i][j]:
                paper(n//2, x, y)
                paper(n//2, x+n//2, y)
                paper(n//2, x, y+n//2)
                paper(n//2, x+n//2, y+n//2)
                return
    if sample == '0':
        white.append(0)
    else:
        blue.append(1)

paper(N, 0,0)
print(len(white))
print(len(blue))