# 2. 3개 더해서 소수만들기
# 배열 nums가 매개변수로 주어진다. nums에 있는 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 수를 return 해라
# nums 숫자 개수는 3개 이상 50개 이하
# nums의 각 원소는 1이상 1000의 자연수, 중복된 숫자가 들어있지 않다

# nums = [1, 2, 3, 4] # 1
nums = [1, 2, 7, 6, 4] # 4

def solution(nums):

    from itertools import combinations

    cases = list(combinations(nums, 3))
    # print(cases)

    def finder(x):
        if x <= 1:
            return False
        else:
            for i in range(2, int(x**0.5)+1):
                if x % i == 0:
                    return False

        return True 
            
    answer = 0
    for case in cases:
        x = sum(case)

        if finder(x):
            answer +=1
    
    return answer

print(solution(nums))

