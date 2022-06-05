# 피보나치 수5
"""
첫째 줄에 n이 주어진다. n은 20보다 작거나 같은 자연수 또는 0이다.
"""

def fibonacci(num):
    if num == 0:
        return 0
    if num == 1 or num ==2:
        return 1
    return fibonacci(num-1)+fibonacci(num-2)

n = int(input())
print(fibonacci(n))
