## https://www.acmicpc.net/problem/1300

# 100,000 * 100,000
# 1 2 3 4 5
# 2 4 6 8 10
# 3 6 9 12 15
# 4 8 12 16 20
# 5 10 15 20 25
# 1, ..., 
k = 10
left = 1 , right = 25
mid = 13
1, 13 -> 7

# 2
# 1, 2, 2, 4
# 3
# 1, 2, 2, 3, 3, 4, 4, 6, 6, 9
# 4
# 1, 2, 2, 3, 3, 4, 4, 4, 6, 6, 8, 8, 9, 12, 12, 16
import math

# N = int(input())
# k = int(input())

k=7
print(int(math.sqrt(k)),int(math.sqrt(k))+1)

k=145 12~13
145-144 = 1 -> 
print(int(math.sqrt(k)),int(math.sqrt(k))+1)