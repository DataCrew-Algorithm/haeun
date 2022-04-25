# 두 수의 합

# Ver1: 메모리 초과
# from itertools import combinations 

# ttl_num = int(input())
# nums = list(map(int, input().split()))
# sum_target = int(input())
# case_list = list(combinations(nums, 2)) # 순서 상관없이 자연수 2개의 조합을 보기 위해

# count = 0
# for case in case_list:
#     if sum(case) == sum_target:
#         count += 1
# print(count)

# Ver2: 시간 초과
# import time
# start_time = time.time()
# import sys
# from itertools import combinations 

# ttl_num = int(input())
# nums = map(int, sys.stdin.readline().split())
# sum_target = int(input())

# count = 0
# for case in combinations(nums, 2):
#     if sum(case) == sum_target:
#         count += 1
# print(count)

# end_time = time.time()
# print("time: ", end_time - start_time)


# Ver.3 투 포인터 알고리즘: 틀림 => interval_sum 필요없음
# from itertools import combinations

# ttl_num = int(input()) # 총 숫자 개수
# nums = sorted(list(map(int, input().split()))) # 전체 수열 오름차순 정렬
# sum_target = int(input()) # 찾고자 하는 부분합

# count = 0
# interval_sum = 0
# end = 0

# # start를 차례대로 증가시키면서 반복
# for start in range(ttl_num):
#     # end를 가능한 만큼 이동 시키기
#     while interval_sum < sum_target and end < ttl_num:
#         interval_sum += nums[end]
#         end += 1
#     if interval_sum == sum_target:
#         count += 1
#     interval_sum -= nums[start]
# print(count)

# Ver.5: 메모리 초과
# import time
# start_time = time.time()

# import sys
# from itertools import combinations 

# ttl_num = int(input())
# nums = map(int, sys.stdin.readline().split())
# sum_target = int(input())
# sum_list = [sum(case) for case in list(combinations(nums, 2))]

# def unpack_sum(data):
#     a, b = map(int, *combinations(nums, 2))
#     return a + b

# print(unpack_sum(nums))

# print(sum_list.count(sum_target)) : 되는 데 메모리 초과

# count = 0
# for case_sum in sum_list:
#     if case_sum == sum_target:
#         count += 1
# print(count)



# # 이진 탐색으로 해보면,
# from bisect import bisect_left, bisect_right

# def count_by_range(list, left_value, right_value):
#     right_index = bisect_right(list, right_value)
#     left_index = bisect_left(list, left_value)
#     return right_index - left_index

# print(count_by_range(sum_list, sum_target, sum_target)) : 되는 데 메모리 초과



# 정답 (투 포인터 알고리즘_풀이 참고)
# 조합의 모든 경우의 수를 구하지 않고도 해결할 수 있다.
# 포인트: 전체 배열의 최솟값, 최댓값 인덱스를 이용하여 포인터를 이동하여 sum을 구하여 조건과 맞는 지 비교
# 두 포인터가 가르키는 숫자의 합이 목표 값보다 크면, end 포인터를 줄이고, 작으면 start 포인터에 +1을 한다.

import sys
input = sys.stdin.readline

ttl_num = int(input()) # 총 숫자 개수
nums = sorted(list(map(int, input().split()))) # 입력 받는 수 리스트 (정렬 해줘야 투 포인터 가능)
sum_target = int(input()) # 찾고자 하는 부분합

count, start, end = 0, 0, ttl_num-1 # 카운트 수, 시작, 끝 포인터 설정

# start를 차례대로 증가시키면서 반복
while True:
    if nums[start] + nums[end] == sum_target:
        count += 1

    # end를 가능한 만큼 이동 시키기
    if nums[start] + nums[end] < sum_target:
        start += 1
    else:
        end -= 1

    if start >= end:
        break
print(count)



