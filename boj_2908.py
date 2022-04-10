# 상수
nums = list(input().split(" "))
new_nums = []

for num in nums:
    new_num = num[::-1]
    new_nums.append(new_num)

print(max(new_nums))



