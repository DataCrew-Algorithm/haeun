list_a = [[1,2,3],[4,5,6], [1,3,4]]
list_b = [0,1,2,3,4,5,6,7,8,9]
m = len(list_b)
i = 0
while True:
    print(list_b[i])
    list_b.pop(0)
    m = len(list_b)
    print(f'-{i}-{m}--')
    if i > m:
        break
    i += 1


# from itertools import combinations_with_replacement
# data = [i for i in range(1, 4)]
# all_com = list(combinations_with_replacement(data, 3))
# print(len(all_com))
# data_1 = [i for i in range(1, 3)]
# not_com = list(combinations_with_replacement(data, 2))
# print(len(data_1))





# 조합을 어떻게 비교할지 생각해보자! 원소가 들어 있는지 파악해야 함
# if s1 & s2 != 0: # 교집합이 있으면
#     print("0")
# else:
#     print("1")


# print(type(not_com[0]))

# s1 = set([1, 2, 3])
# s2 = set([1, 3])

# print(len(s1 - s2))

# if s1 & s2 != 0:
#     print("0")
# else:
#     print("1")