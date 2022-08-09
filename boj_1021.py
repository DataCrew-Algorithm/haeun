# Rotating Queue (92ms)
# 1번 연산: popleft()
# 2번 연산: 왼쪽 1칸 이동
# 3번 연산: 오른쪽 1칸 이동
# 2번, 3번 연산의 최솟값

from collections import deque

N, M = map(int, input().split()) # 큐의 크기, 뽑아내려고 하는 수의 개수 
nums = deque(i for i in range(1, N+1))
loc = list(map(int, input().split())) # 처음 큐에서의 위치
# print(nums)
# print(loc)

cnt = 0

for num in loc:
    while loc:
        if nums[0] == num:
            nums.popleft()
            # print(nums)
            break

        else:
            if nums.index(num) <= len(nums) // 2: # 위치값이 전체길이의 절반보다 작으면 왼쪽이동
                nums.rotate(-1)
                # print(nums)
                cnt += 1
            else:
                nums.rotate(1)
                # print(nums)
                cnt += 1
print(cnt)