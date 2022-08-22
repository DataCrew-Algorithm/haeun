# 동전 1
# n 가지 동전 종류,  합은 k원 (target), 경우의 수? 동전 개수 제한 없음
# 동전의 구성이 같은데 순서만 다른 것 =  같은 경우 (순서상관 없음)

# target 합의 경우의 수로 분기하면서 경우의 수가 나올 때 cnt 하려고 했는데 경우의 수가 너무 많음!
n, k = map(int, input().split())
val = [int(input()) for _ in range(n)]
print(val)

def SplitNum(list):
    global k
    combs = []
    for a in range(1, k//2 + 1):
        b = k - a
        combs.append([a, b])

    return combs # [[1, 9], [2, 8], [3, 7], [4, 6], [5, 5]]

combs = SplitNum(val)
cnt = 0
for comb in combs:
    if comb[0] and comb[1] > 0:
        for j in val:
            if comb[0] % j == 0 or comb[1] % j == 0:
                cnt += 1
            else:
                if comb[0] % j != 0:
                    k = comb[0] - 1
                    print(k)
                    print(SplitNum(comb))
                    
                if comb[1] % j != 0:
                    k = comb[1] - 1
                    print(k)
                    print(SplitNum(comb))
        # elif comb[0] > 2 or comb[1] > 2:
        #     if (comb[0] - 1) % j == 0 or (comb[1] - 1) % j == 0:
        #         cnt += 1
print(cnt)



# ver.1 실패
# count = 0
# for coin in val:
#     count += k // coin
#     k %= coin

# print(count)

# 정답 --> dp 계산결과를 저장하는 테이블, 2중 포문 돌면서 d[i] 위치에 d[k-i] 값을 누적하면서 갱신
n, k = map(int, input().split())
c = []
dp = [0 for i in range(k + 1)]
dp[0] = 1 # 동전의 수가 1개일 때 고려
for i in range(n):
    c.append(int(input()))
for i in c:
    for j in range(1, k + 1):
        if j - i >= 0:
            dp[j] += dp[j - i]
print(dp[k])