# 이항 계수 1
""" 
자연수 \(N\)과 정수 \(K\)가 주어졌을 때 이항 계수 
\(\binom{N}{K}\)를 구하는 프로그램을 작성하시오.
"""

N, K = map(int, input().split())

K = min([K, N-K])
sum = 1
for i in range(K):
    sum =sum*(N-i)/(i+1) 
print(int(sum))