# Maximum Subarray
# Subarray 연속 수열의 누적합 중 최댓값은??
# DP 이용

# nums = [-2,1,-3,4,-1,2,1,-5,4] # 6
# nums = [1] # 1
nums = [5,4,-1,7,8] # 23

# print(len(nums))
# 음수의 영향을 최소화하는 방향으로 해야 합이 최댓값

# ver1. 868ms
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        for i in range(1, len(nums)): 
            nums[i] += nums[i-1] if nums[i-1] > 0 else 0
        
        return max(nums)

Sol = Solution()
print(Sol.maxSubArray(nums))

# ver2. 658ms! 최댓값 갱신하면서 푸는 것이 더 빠름

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = partial_sum = nums[0]

        for i in range(1, len(nums)): 
            partial_sum = max(nums[i], nums[i]+partial_sum)
            max_sum = max(partial_sum, max_sum) # 최댓값을 갱신
        
        return max_sum

Sol = Solution()
print(Sol.maxSubArray(nums))


