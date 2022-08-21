# 포도주 시식
# 효주가 마실 수 있는 최대 포도주의 양??

import sys
input = sys.stdin.readline

n = int(input())
wine_qty = [0]+[int(input()) for _ in range(n)] # dp랑 자리 수 맞추기
# print(wine_qty)

dp = [0]*(n+1)
dp[0] = wine_qty[0]
dp[1] = wine_qty[1]

# 3가지 경우의 수 고려: 현재 포도주 안 마심 / 앞 포도주 마시고 현재 포도주 마심 / 앞 포도주 안 마시고 현재 포도주 마심
if n > 1:
    dp[2] = wine_qty[1] + wine_qty[2]

for i in range(3, n+1):
    dp[i] = max(dp[i-2] + wine_qty[i], dp[i-3] + wine_qty[i-1] + wine_qty[i], dp[i-1])

# print(dp)
print(max(dp))

