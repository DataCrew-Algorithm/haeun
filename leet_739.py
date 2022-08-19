# Daily Temperatures
# 스택과 인덱스를 활용하여 현재 기온보다 높을 때까지 며칠 걸리는지 확인


temperatures = [73,74,75,71,69,72,76,73]

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
        answer = [0] * len(temperatures)
        stack = []
        
        for i, cur in enumerate(temperatures):
                   
            # 현재 온도가 높을 때만 갱신
            while stack and cur > temperatures[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last # 현재 인덱스 - 스택에 쌓아둔 현재 온도 값
                
            stack.append(i)
            
        return answer


Sol = Solution()
print(Sol.dailyTemperatures(temperatures))
