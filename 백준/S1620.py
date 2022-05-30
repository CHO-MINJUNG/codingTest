# 나는야 포켓몬 마스터 이다솜
"""
"""

N, M = map(int, input().split())

engDict = {}
numDict = {}

for i in range(N):
    name = input()
    engDict[name] = i+1
    numDict[str(i+1)] = name

for i in range(M):
    question = input()
    try:
        num = int(question)
        print(numDict[question])
    except:
        print(engDict[question])