# 부당한 퍼즐

# Ver.1: 틀림
from collections import deque
n = int(input())
nums = list(map(int,input().split(" ")))
check_nums = deque(map(int,input().split(" ")))

while nums != check_nums: # 다를 때만 반복
    last_num = check_nums.pop()
    check_nums.appendleft(last_num) 
    new = list(reversed(check_nums))
    
    if nums == new:
        print("good puzzle")
        break
    else:
        print("bad puzzle")
        break

# Ver2. 통과 (676ms)
n = int(input())
nums = list(map(int,input().split(" ")))
check_nums = list(map(int,input().split(" ")))

idx = check_nums.index(nums[0])                         
new_list1 = check_nums[idx:] + check_nums[:idx]             # 순방향 체크

r_check_nums = check_nums[::-1]
idx2 = r_check_nums.index(nums[0])
new_list2 = r_check_nums[idx2:] + r_check_nums[:idx2]       # 역방향 체크

if nums == new_list1 or nums == new_list2:
    print("good puzzle")
    
else:    
    print("bad puzzle") 

# Ver3. 통과 (884ms)

import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
compare_nums = list(map(int, input().split()))

first_idx = compare_nums.index(nums[0]) # 0번째자리를 처음 기준점으로 봄
new_list1 = []
new_list2 = []

# 순방향인 경우
start = first_idx - N
end = first_idx

for i in range(start, end):
    new_list1.append(compare_nums[i])

# 역방향인 경우
start = first_idx
end = first_idx - N

for i in range(start, end, -1):
    new_list2.append(compare_nums[i])

# 둘 중 하나 맞으면 good puzzle
if nums == new_list1 or nums == new_list2:
    print("good puzzle")
else:
    print("bad puzzle")
