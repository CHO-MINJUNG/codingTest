#약수
"""
양수 A가 N의 진짜 약수가 되려면, N이 A의 배수이고, A가 1과 N이 아니어야 한다. 
어떤 수 N의 진짜 약수가 모두 주어질 때, N을 구하는 프로그램을 작성하시오.
"""

cnt = int(input())
num_list = list(map(int, input().split()))
sort_list = sorted(num_list)
print(sort_list[0]*sort_list[-1])

# max(num_list)*min(num_list) 하는 방법도 있었음! 완전 good