# Trapping Rain Water
# 비온 후 얼마나 배수구에 비가 차는지 구하라
# height는 블록의 높이

height = [0,1,0,2,1,0,1,3,2,1,2,1]

# Output: 6

# Ver.1 => 오답: 다시 짜보기
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        walls = []
        max_num = height[0]
        count  = 0
        for i in range(len(height)):
            # if height[i] > 0 :
            #     walls.append(height[i])
            if max_num <= height[i]: # 최댓값이 새로운 높이 보다 작으면 갱신
                max_num = height[i]
                count += height[i] - max_num # 최댓값 높이 - 이전 최댓값 = 빗물
                # print(count)
            else:
                count += abs(height[i] - height[i-1]) # 최댓값 높이 - 이전 최댓값 = 빗물
                # print(count)
        return count

Sol = Solution()
print(Sol.trap(height))


# Ver2. 투 포인터 활용: 139ms
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        volume = 0
        left, right = 0, len(height) - 1
        left_max = height[left]
        right_max = height[right]

        
        while left < right:
            left_max = max(height[left], left_max)
            right_max = max(height[right], right_max)

            if left_max <= right_max:                  # 오른쪽영역 최댓값이 왼쪽 영역 최댓값 보다 클 때 오른쪽 포인터 왼측이동
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]    # 왼쪽영역 최댓값이 오른쪽 영역 최댓값 보다 클 때 왼쪽 포인터 우측이동
                right -= 1 
            
        return volume

Sol = Solution()
print(Sol.trap(height))