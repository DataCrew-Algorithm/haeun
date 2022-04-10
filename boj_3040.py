# 백설공주_난쟁이 7명 찾기
# 조합 내장함수 이용 (iterable 자료 중 몇개 뽑는지 체크)
# 문제에서는 7개 숫자 추출
# 다 더했을 때 100이면 반복을 추출한 수를 출력하고 중단

from itertools import combinations
nums = [int(input()) for i in range(9)]

for i in combinations(nums, 7):
    if sum(i) == 100:
        print(*i, sep= "\n")
        break






# nums = [int(input()) for i in range(9)]
# def add_num(list):
#     num = 0
#     for idx, i in enumerate(nums):
#         num += i
#         print(num)
#         if num == 100:
#             print(idx)
            