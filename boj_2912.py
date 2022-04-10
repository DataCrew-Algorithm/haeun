# 백설공주와 난쟁이
# (3 ≤ N ≤ 300,000, 1 ≤ C ≤ 10,000)
# 1 ≤ M ≤ 10,000

# ver1 시간초과
# dwarf, color_num = map(int, input().split())     # 난쟁이 수, 모자 색상 수
# color = list(map(int, input().split()))          # 모자 색 리스트
# pic_nums = int(input())                          # 사진 수

# for i in range(pic_nums):
#    start_df, end_df = map(int, input().split())
#    check = color[start_df-1:end_df] 
#    standard = len(check) / 2
#    count = []

#    for j in range(1, color_num+1):
#        count.append(check.count(j))
#        if check.count(j) > standard:
#            print(f"yes {j}")
#    if max(count) <= standard:
#        print("no") 
            

# no를 1번만 하게 하려면...
# 시간 단축하기
dwarf, color_num = map(int, input().split())     # 난쟁이 수, 모자 색상 수
color = list(map(int, input().split()))          # 모자 색 리스트
pic_nums = int(input())                          # 사진 수

for j in range(1, color_num+1):
    count = []
    count.append(check.count(j))

for i in range(pic_nums):
    start_n, end_n = map(int, input().split())
#    check = color[start_n-1:end_n] 
#    standard = len(check) / 2
    if check.count(j) > standard:
        print(f"yes {j}")
        break
if max(count) <= standard:
    print("no") 
            











       
# for i in range(pic_nums):
#    start_df, end_df = map(int, input().split())
#    check = color[start_df-1:end_df] 
#    std = len(check) / 2
#    sum_num = 0

#    for j in range(1, color_num+1):
#        sum_num += check.count(j)

#        if sum_num >= len(check):
#            print(f"yes {j}")
#            break

#        else:
#            print("no")

    
# list = [1, 2, 2, 3, 3, 3, 4]
# count =[]
# for i in list:
#     if list.count(i) >= 2:
#         count.append(list.count(i))
# max_num = max(count)
# print(max_num)
