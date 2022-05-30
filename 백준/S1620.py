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

""" 
isdigit() 이란 함수로 숫자인지 문자열인지 
판단할 수 있는 method를 알게됨
-> 근데 시간이 더 걸림 
5356 -> 6928
"""

# for i in range(M):
#     question = input()
#     if question.isdigit():
#         print(numDict[question])
#     else:
#         print(engDict[question])