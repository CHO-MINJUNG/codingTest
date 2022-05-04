#최대공약수와 최소공배수
"""
두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.
"""

# a, b = map(int, input().split())
# maxNum=1
# for i in range(1,max([a,b])+1):
#     if (a%i==0) & (b%i==0):
#         maxNum=i
# print(maxNum) 
# print((a*b)//maxNum)

# maxNum을 0부터 시작한 실수
# range 범위 제대로 생각 못한 실수

## 유클리드 호제법 사용해보기

def GCD(abList):
    maxNum = max(abList)
    minNum = min(abList)
    return minNum, maxNum%minNum 

a, b = map(int, input().split())
new = a*b
gong= 1
while True:
    if a==0 or b==0:
        gong = max([a,b])
        break
    a, b = GCD([a,b])

print(gong) 
print(new//gong)