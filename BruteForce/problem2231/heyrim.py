# 분해합의 생성자를 구하는 코드

Number_s = input()
Number = int(Number_s)
re_num = 0

for i in range(1, Number):
    i_num = i
    list_number = list(str(i))

    for num in list_number:
        i_num += int(num)

    if (i_num == Number):
        re_num = i
        break
    
    else:
        re_num = 0
    
print(re_num)


# 리스트를 sum해서 풀기

Number_s = input()
Number = int(Number_s)
re_num = 0

for i in range(1, Number):
    list_number_i = [int(x) for x in list(str(i))]
    i_num = i + sum(list_number_i)

    if (i_num == Number):
        re_num = i
        break
    
    else:
        re_num = 0
    
print(re_num)