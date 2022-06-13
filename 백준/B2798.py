# 블랙잭
"""
첫째 줄에 카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000)이 주어진다. 둘째 줄에는 카드에 쓰여 있는 수가 주어지며, 이 값은 100,000을 넘지 않는 양의 정수이다.

합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력으로 주어진다.
"""

N, M = map(int, input().split())
cards = list(map(int, input().split(" ")))
cnt = len(cards)
result = 0
for i in range(cnt-2):
    for j in range(i+1, cnt-1):
        for z in range(j+1, cnt):
            ex = cards[i] + cards[j] + cards[z]
            if ex<=M:
                result = max(result, ex)

print(result)
