# 음계
# input_num = input()
# num_sorted = "1 2 3 4 5 6 7 8"
# num_sortedr = "8 7 6 5 4 3 2 1"

# if input_num == num_sorted:
#     print("ascending")
# elif input_num == num_sortedr:
#     print("descending")
# else:
#     print("mixed")

# ver.2

input_num = input().split() # 디폴트값이 공백
num_sorted = [str(i) for i in range(1, 9)] # 문자열로 형태 맞춰주기
num_sortedr = num_sorted[::-1]

if input_num == num_sorted:
    print("ascending")
elif input_num == num_sortedr:
    print("descending")
else:
    print("mixed")

# ver.3
# input_num = input().split(" ")
# num_sorted = [str(i) for i in range(1, 9)] # 문자열로 형태 맞춰주기

# if input_num == num_sorted:
#     print("ascending")
# elif input_num == list(reversed(num_sorted)):
#     print("descending")
# else:
#     print("mixed")