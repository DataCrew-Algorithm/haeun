# Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
nums = [2, 7, 11, 15]
target = 9

from typing import List 
# from itertools import combinations => 반례 케이스로 인해 실패
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         c_list = list(combinations(nums, 2))
#         for a, b in c_list:
#             if a + b == target:
#                 return [nums.index(a), nums.index(b)]
#                 break

# Sol = Solution()
# print(Sol.twoSum(nums, target))

# from itertools import combinations
# c_list = list(combinations(nums, 2))
# for a, b in c_list:
#     print(a, b)
#     if a + b == target:
#         print([nums.index(a), nums.index(b)])
#         break



# Ver2.enumerate와 딕셔너리를 활용하자 (118ms)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i, num in enumerate(nums): 
            print(i, num)
            if target - num in nums_dict:
                return [nums_dict[target - num], i]
            nums_dict[num] = i


# Sol = Solution()
# print(Sol.twoSum(nums, target))

# Ver3.이중for문 사용 가능: 4890 ms

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
Sol = Solution()
print(Sol.twoSum(nums, target))

# 투포인터를 이용한 풀이!! (수현님 풀이 참고): 74ms
class Solution:
    def twoSum(self, nums, target):
        left = 0
        right = len(nums)-1
        nums_s = sorted(nums)   # sort 해놓은 것을 새로 담음
        while left < right:
            if nums_s[left] + nums_s[right] < target:  # 타겟보다 작으면 왼쪽 포인터 +1
                left += 1
            elif nums_s[left] + nums_s[right] > target: # 타겟보다 크면 오른쪽 포인터 -1
                right -= 1
            else:                                       # 같으면 멈춤
                break
        if nums_s[left] == nums_s[right]:               # 값이 같은 경우에 [3,2,3]
            left_ = nums.index(nums_s[left])            # 처음 나오는 값의 인덱스를 left_에 담고
            nums[left_] = '*'                           # 또 발견되면 안되니까 *로 바꿔주고 [*, 2, 3]
            right_ = nums.index(nums_s[right])          # 두번째 나오는 값의 인덱스를 right_에 담음
        else:
            left_ = nums.index(nums_s[left])            # 값이 같은 경우가 아닌 경우라면 *로 안 바꿔주고 그냥 담으면 됨
            right_ = nums.index(nums_s[right])
        return [left_, right_]



# nums = [3, 2, 3]
# target = 6 => [0, 1]

sol = Solution()
print(sol.twoSum(nums, target))
