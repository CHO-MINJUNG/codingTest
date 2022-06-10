# LCS
"""
LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.
"""

def LCS(a, b):
    num = 0
    lcs = [[0]*(len(b)+1) for _ in range(len(a)+1)]
    for i in range(1,len(a)+1):
        for j in range(1,len(b)+1):
            if a[i-1]==b[j-1]:
                lcs[i][j]=lcs[i-1][j-1]+1
                num = max(lcs[i][j], num)
            else:
                lcs[i][j]=max(lcs[i][j-1],lcs[i-1][j])
    print(num)

A = input()
B = input()

LCS(A, B)