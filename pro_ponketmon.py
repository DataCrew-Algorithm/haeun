# 프로그래머스 폰켓몬 (해쉬 문제): https://school.programmers.co.kr/learn/courses/30/lessons/1845#qna
# 가장 많은 종류의 폰켓몬을 선택하는 방법이 여러 가지인 경우에도, 
# 선택할 수 있는 폰켓몬 종류 개수의 최댓값 하나만 return 하면 됩니다.

# ver.1: 실패 --> 다른 테스트 케이스에서 막힘

from itertools import combinations

nums = [3, 3, 3, 2, 2, 2]

# def solution(nums):
cases = list(combinations(nums, len(nums)//2))

check = []
for case in cases:
    # print(case)
    
    cnt = []
    for i in case:
        print(i)
        if cnt[-1:] == [i]: continue
        cnt.append(i)
    # print(cnt)
    check.append(len(cnt))
# print(check)
print(max(check))

# ver2: 참고 풀이1
# 경우의 수가 종류의 수 이상일 때를 조건으로 바로 판별하면 되는 문제였다.

def solution(nums):
    
    choice_cnt = int(len(nums)/2) # 조합 수
    kind_cnt = len(list(set(nums))) # 종류의 수
    result = 0 

    if choice_cnt >= kind_cnt:
        result = kind_cnt
    else:
        result = choice_cnt


    return result

# ver3: 참고 풀이2
# 최댓값에 낚이지 말고 예시 결과 보게 되면 최솟값으로 구해도 답 나옴!!

def solution(ls):
    return min(len(ls)/2, len(set(ls)))
