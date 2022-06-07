# 균형잡힌 세상
"""
하나 또는 여러줄에 걸쳐서 문자열이 주어진다. 각 문자열은 영문 알파벳, 공백, 소괄호("( )") 대괄호("[ ]")등으로 이루어져 있으며, 길이는 100글자보다 작거나 같다. 각 줄은 마침표(".")로 끝난다.

입력의 종료조건으로 맨 마지막에 점 하나(".")가 들어온다.
"""
import sys

while True :
    str = sys.stdin.readline().rstrip()
    if str==".":
        break
    stack = []*100
    allIterate = True
    # ( = 0 , [ = 1
    for i in list(str):
        if i == "(":
            stack.append(0)
        elif i == "[":
            stack.append(1)
        elif i == ")":
            if stack==[]:
                allIterate=False
                break
            stackLast = stack.pop()
            if stackLast != 0:
                allIterate=False
                break
        elif i == "]":
            if stack==[]:
                allIterate=False
                break
            stackLast = stack.pop()
            if stackLast != 1:
                allIterate=False
                break
    if stack == [] and allIterate==True:
        print('yes')
    else:
        print('no')