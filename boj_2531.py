# 회전초밥
# 접시의 수 N, 초밥의 가짓수 d, 연속해서 먹는 접시의 수 k, 쿠폰 번호 c
# c 쿠폰에 적힌 초밥은 무조건 먹게 됨
# k를 연속적으로 먹을 때, 손님이 먹을 수 있는 초밥 가짓수의 최댓값

# ver1. 경우의 수를 집합으로 처리하여 중복제거! -- 시간초과

import sys
read = sys.stdin.readline

N, d, k, c = map(int, input().split())
chain = []
for _ in range(N):
    chain.append(int(read().rstrip()))
# print(chain)
# Two Pointer 
lp, rp = 0, 0
answer = 0

while lp != N:
    rp = lp + k
    case = set()
    addable = True # 추가 가능여부
    for i in range(lp, rp): 
        i %= N # 위치를 나머지 값으로 구함
        case.add(chain[i])
        if chain[i] == c:
            addable = False # 쿠폰번호가 나오면 추가 x (어차피 먹게 되므로)

    cnt = len(case)
    if addable: cnt += 1
    answer = max(answer, cnt)
    lp += 1 
# print(answer)


# ver2. defalutdict 활용 참고 풀이 (https://juhi.tistory.com/18) -- 128ms
# 회전 초밥이라서 0~k, n-1~k-1까지 순환 가능

from collections import defaultdict
import sys
read = sys.stdin.readline

N, d, k, c = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(read().rstrip()))

case = defaultdict(int)
cnt = 1 # 무조건 먹게 되는 초밥 1개
case[c] = 1
print(case) # defaultdict(<class 'int'>, {30: 1})

for i in range(k):
    if case[arr[i]] == 0:
        cnt += 1
    case[arr[i]] += 1

answer = cnt
for left in range(N):
    right = (left + k) % N
    case[arr[left]] -= 1
    if case[arr[left]] == 0:
        cnt -= 1
    if case[arr[right]] == 0:
        cnt += 1
    case[arr[right]] += 1
    answer = max(answer, cnt)
# print(case)
print(answer)


