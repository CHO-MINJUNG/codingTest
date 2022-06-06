# 파도반 수열
"""
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. (1 ≤ N ≤ 100)
"""

padoL=[1,1,1,2,2]
for i in range(95):
    padoL.append(padoL[i]+padoL[i+4])

cnt = int(input())
for i in range(cnt):
    num = int(input())
    print(padoL[num-1])


#------------------------------------
# append를 index로 접근하게 하니까 시간을 28ms 줄였음 메모리는 그대로

padoL = [0 for i in range(100)]
padoL[0]=1
padoL[1]=1
padoL[2]=1
padoL[3]=2
padoL[4]=2
for i in range(95):
    padoL[i+5]=padoL[i]+padoL[i+4]

cnt = int(input())
for i in range(cnt):
    num = int(input())
    print(padoL[num-1])