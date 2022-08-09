# 토너먼트
# 김지민과 임한수가 몇 라운드에서 대결하는지 출력 (만나기 전까지 항상 이김)
# 서로 대결하지 않으면 -1 출력

# N >= 2, N <= 100,000

# N, j, h = map(int, input().split()) # 전체 참가자 수, 1라운드 지민-한수 번호

# cnt = 1 # round 숫자
# nums = [i for i in range(1, N+1)] 
# fights = []

# for i in range(0, len(nums) - 1, 2):
#     fights.append([nums[i], nums[i+1]])
# print(fights)


# if [j, h] in fights:
#     print(cnt)
# else:
#     print(-1)


# 참고풀이 72ms :

import sys

n, kim, lim = map(int, sys.stdin.readline().split())
cnt = 0

# 만났는지를 비교해서 안 만났으면 진 사람들을 제외하고 위치를 초기화함
while kim != lim:
    kim -= kim // 2
    lim -= lim // 2
    cnt += 1 

print(cnt)


