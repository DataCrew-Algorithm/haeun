# 소수 만들기 (https://school.programmers.co.kr/learn/courses/30/lessons/12977)
# num에 주어지는 숫자 중 3개를 더했을 때 소수인 경우의 개수

# from itertools import combinations

# nums = [1, 2, 7, 6, 4]
# def solution(nums):
#     cases = list(combinations(nums, 3))
#     case_sum = list(set([sum(i) for i in cases]))

#     # 모두 소수라고 초기화
#     arr = [True for _ in range(len(case_sum)+1)]  
#     div_num = 2
#     # answer = 0
#     for sum_v in case_sum:
#         if sum_v % div_num == 0:
#             arr[sum_v] = False


#     return print(sum(arr))

# print(solution(nums))

from itertools import combinations

# 아리스토텔레스의 체 반환
def aristoSieve(size):
    # 초기화
    aristo = [True] * (size + 1)
    aristo[0], aristo[1] = False, False
    
    # 1 ~ 1000까지의 아리스토텔레스의 체
    for i in range(2, int(size ** 0.5) + 1): # 메모리 사용 단축하기 위해 제곱근 사용
        if aristo[i] == True:
            for j in range(i + i, size + 1, i):
                aristo[j] = False
                
    return aristo

# 솔루션 함수
def solution(nums):
    answer = 0
    # 아리스토 체 생성
    aristo = aristoSieve(3000)
    # 숫자 3개를 조합해서 나오는 것을 출력
    combi = list(combinations(nums, 3))
    
    for case in combi:
        if aristo[sum(case)]:
            answer += 1

    return answer

nums = [1, 2, 7, 6, 4]
print(solution(nums))


# 내가 풀려고 했던 방식: for문 구간 설정하는 거에서 cand로 하고
# 소수면 카운팅해서 더함

def solution(nums):
    from itertools import combinations as cb
    answer = 0
    for a in cb(nums, 3):
        cand = sum(a)
        for j in range(2, cand):
            if cand % j == 0:
                break
        else:
            answer += 1
    return answer