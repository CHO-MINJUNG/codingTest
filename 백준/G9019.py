# acmicpc.net/problem/9019

def double(num):
    return 10000%(num*2)

def subtract(num):
    if num==0:
        return 9999
    else :
        return num-1        

def leftRotate(num):
    if len(str(num)) < 4 :
        num = ('0'*(4-len(str(num))))+str(num)
    l = list(str(num))
    a = l.pop(0)
    l.append(a)
    return(int(''.join(l)))

def rightRotate(num):
    if len(str(num)) < 4 :
        num = ('0'*(4-len(str(num))))+str(num)
    l = list(str(num))
    a = l.pop()
    l.insert(0, a)
    return(int(''.join(l)))

cnt = int(input())
for i in range(cnt):
    a, b = list(map(int, input().split()))
    testCase = []
    result = []

    testCase.append(double(a))
    result.append('D')
    testCase.append(subtract(a))
    result.append('S')
    testCase.append(leftRotate(a))
    result.append('L')
    testCase.append(rightRotate(a))
    result.append('R')

    while True:
        if testCase.pop(0) == b:
            print(result.pop(0))
            break
        nowNum = testCase.pop(0)
        nowResult = result.pop(0)
        testCase.append(double(nowNum))
        result.append(nowResult+'D')
        testCase.append(subtract(nowNum))
        result.append(nowResult+'S')
        testCase.append(leftRotate(nowNum))
        result.append(nowResult+'L')
        testCase.append(rightRotate(nowNum))
        result.append(nowResult+'R')