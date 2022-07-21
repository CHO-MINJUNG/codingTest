# 단어 정렬
"""
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

길이가 짧은 것부터
길이가 같으면 사전 순으로
"""
import sys

cnt = int(sys.stdin.readline())

words = [[] for _ in range(50)]

for i in range(cnt):
    str = sys.stdin.readline().rstrip()
    words[len(str)-1].append(str)
# words = list(set(words))

# words.sort()
for i in words:
    if i == []:
        continue
    i = list(set(i))
    i.sort()
    for j in i:
        print(j)
    