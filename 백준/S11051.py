# 이항 계수 2
"""
자연수 \(N\)과 정수 \(K\)가 주어졌을 때 이항 계수 
\(\binom{N}{K}\)를 10,007로 나눈 나머지를 구하는 프로그램을 작성하시오.
"""
from fractions import Fraction

N, K = map(int, input().split())

K = min([K, N-K])
sum = 1
for i in range(K):
    sum =sum*(N-i)*Fraction(1, (i+1))
print(sum%10007)