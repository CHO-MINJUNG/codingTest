#패션왕 신해빈
"""
해빈이는 패션에 매우 민감해서 한번 입었던 옷들의 조합을 절대 다시 입지 않는다. 예를 들어 오늘 해빈이가 안경, 코트, 상의, 신발을 입었다면, 다음날은 바지를 추가로 입거나 안경대신 렌즈를 착용하거나 해야한다. 해빈이가 가진 의상들이 주어졌을때 과연 해빈이는 알몸이 아닌 상태로 며칠동안 밖에 돌아다닐 수 있을까?
"""

cnt = int(input())
for i in range(cnt):
    kinds_dict = {}
    cnt2 = int(input())
    mul_sum=1
    for j in range(cnt2):
        kinds =  input().split()[1]
        if kinds in kinds_dict:
            kinds_dict[kinds] +=1
        else:
            kinds_dict[kinds] = 1

    value_list = list(kinds_dict.values())
    if len(value_list) ==1:
        print(value_list[0])
        continue
    for j in value_list:
        mul_sum *= (j+1)
    print (mul_sum-1)

# Counter라는 라이브러리 사용하면 list의 요소 갯수를 세어서 list로 반환해준다..!