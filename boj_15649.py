# N과 M(1): 수열 구하기
from itertools import permutations

n, m = map(int, input().split())

if m == 1:
    for i in range(1, n+1):
        print(i)
else:
    num_pick = list(permutations([i for i in range(1, n+1)], m))
    for pair in num_pick:
        print(*pair)