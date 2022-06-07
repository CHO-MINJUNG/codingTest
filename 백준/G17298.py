# 오큰수
"""
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에 수열 A의 원소 A1, A2, ..., AN (1 ≤ Ai ≤ 1,000,000)이 주어진다.
"""


size = int(input())
stack = []*size
result = []
A = list(map(int, input().split(" ")))
A.reverse()
for i in A:
    for j in range(len(stack),0,-1):
        if stack[j-1]<=i:
            stack.pop()
        else:
            result.append(stack[j-1])
            stack.append(i)
            break
    if stack==[]:
        result.append(-1)
        stack.append(i)
        continue
    
result.reverse()
print(' '.join(map(str,result)))