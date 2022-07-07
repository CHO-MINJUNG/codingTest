# 검문
"""
트럭을 타고 이동하던 상근이는 경찰의 검문을 받게 되었다. 경찰은 상근이가 운반하던 화물을 하나하나 모두 확인할 것이기 때문에, 검문하는데 엄청나게 오랜 시간이 걸린다.

상근이는 시간을 때우기 위해서 수학 게임을 하기로 했다.

먼저 근처에 보이는 숫자 N개를 종이에 적는다. 그 다음, 종이에 적은 수를 M으로 나누었을 때, 나머지가 모두 같게 되는 M을 모두 찾으려고 한다. M은 1보다 커야 한다.

N개의 수가 주어졌을 때, 가능한 M을 모두 찾는 프로그램을 작성하시오.
"""
def GCD(abList):
    funcList = abList[:]
    while True:
        funcList.sort()
        if funcList[-1]==funcList[0]:
            return funcList[0]
        funcList[-1] = funcList[-1] - funcList[0]
        
    
cnt = int(input())
nList= [int(input()) for _ in range(cnt)]
result = []
minNum = min(nList)
for i in range(minNum):
    nList = [x+1 for x in nList]
    num = GCD(nList)
    if num!=1:
        result.append(num)
result = list(set(result))
result.sort()
print(' '.join(map(str, result)))
# def maxDivisor(newL):
#     if len(newL)==1:
#         return newL[0]
#     new=[]
#     if len(newL)%2 ==0:
#         for i in range(0,len(newL),2):
#             a, b = newL[i], newL[i+1]
#             gong= 1
#             while True:
#                 if a==0 or b==0:
#                     gong = max([a,b])
#                     new.append(gong)
#                     break
#                 a, b = GCD([a,b])
#         return maxDivisor(new)
#     else:
#         for i in range(0,len(newL)-1,2):
#             a, b = newL[i], newL[i+1]
#             gong= 1
#             while True:
#                 if a==0 or b==0:
#                     gong = max([a,b])
#                     new.append(gong)
#                     break
#                 a, b = GCD([a,b])
#             new.append(newL[-1])
#         return maxDivisor(new)    

# cnt = int(input())
# nList= []*100
# for i in range(cnt):
#     nList.append(int(sys.stdin.readline()))

# output = []
# for i in range(min(nList)):
#     divisionList = [j-i for j in nList]
#     maxdivisor = maxDivisor(divisionList)
#     if maxdivisor != 1:
#         output.append(maxdivisor)

# print(' '.join(map(str,set(output))))
