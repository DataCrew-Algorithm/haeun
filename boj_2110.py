# 공유기 설치 (골드4)
# 가장 인접한 2개의 공유기 사이의 최대 거리를 구해라

import sys
input = sys.stdin.readline

N, C = map(int, input().split())
site = [int(input()) for _ in range(N)]

# 정렬하기
site.sort()
print(site)

# 이진탐색법으로 범위의 중간점에서 시작해서 최대 길이가 포함된 공유기 전체 댓수를 
# 설치 할 수 있는지 체크

start = 1 # 가능한 최소 거리 (min gap)
end = site[-1] - site[0] # 가능한 최대거리
result = 0

while (start <= end):
    mid = (start + end) // 2 # 가운데 좌표 (몫)
    count = 0

    # 현재 mid 값을 이용해 공유기 설치 (i가 0일 때 분류 안 해주면 런타임 에러)
    for i in range(N):
        if i == 0:
            value = site[i]
            count += 1

        else:
            if site[i] >= value + mid:
                value = site[i]
                count += 1
        
    if count >= C:  # c 개 이상 공유기를 설치할 수 있는 경우, 거리 증가
        start = mid + 1
        if result < mid:
            result = mid # 최적의 결과 저장
    
    else:           # c 개 이상 공유기를 설치할 수 있는 경우, 거리 감소
        end = mid - 1

print(result)
