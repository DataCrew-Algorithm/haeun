# 계단 오르기!

# ver.1 (예시 케이스는 맞지만) 실패
# import sys
# read = sys.stdin.readline

# n = int(input())
# scores = [int(read()) for _ in range(n)]
# # print(scores)

# d = [0] * (n-2) # 300개 이하 자연수, 처음과 끝을 빼서
# d[0] = scores[0]
# d[1] = max(scores[0], scores[1])
# d[-1] = scores[-1]

# for i in range(2, n):
#     # d[i+1] = max(d[i-1], d[i-2] + scores[i])
#     # d[i+1] = d[i-2] + max(scores[i-1], scores[i])
#     d[i+1] = d[i] + max(scores[i], scores[i-2])

#     # print(d[i+1])

# answer = d[n-1] + scores[-1]
# print(answer)



# ver2. 계단의 짝수 홀수로 구분해서 생각 ==> Index Error
# import sys
# read = sys.stdin.readline

# n = int(input())
# scores = [int(read()) for _ in range(n)]
# # print(scores)

# d = [0] * n # 300개 이하 자연수, 처음과 끝을 빼서
# d[0] = scores[0]
# d[1] = max(scores[0], scores[1])
# # d[-1] = scores[-1]

# if n % 2 == 0:
#     for i in range(2, n):
#         d[i+1] = d[i] + max(scores[i], scores[i-2])
#         print(d[i+1])

#     answer = d[n-1] + scores[-1]
#     print(answer)

# else:
#     for i in range(2, n):
#         d[i+1] = d[i] + max(scores[i], scores[i-2])
#     print(d[n-1])


# ver3. 인터넷 참고 풀이: 직전 칸이 n-1인지 n-2인지 생각하기

# import sys
# read = sys.stdin.readline

# n = int(input())
# scores = [int(read()) for _ in range(n)]
# print(scores)

# 계단 1-3개 일때 입력해보면 2개일때 인덱스 에러나서 런타임 에러 발생!!
# d = []
# d.append(scores[0])
# d.append(max(scores[0] + scores[1], scores[1]))
# d.append(max(scores[0] + scores[2], scores[1] + scores[2]))

# 이 풀이도 인덱스 에러남!
# d = []
# d.append(scores[0])
# for i in range(1, 3):
#     if i == 1:
#         d.append(max(d[i-1] + scores[i], scores[i]))
#     continue
#     d.append(max(d[i-2] + scores[i], d[i-1] + scores[i]))

# for i in range(3, n):
#     d.append(max(scores[i] + scores[i-1] + d[i-3], scores[i] + d[i-2]))

# print(d[-1])


import sys

input = sys.stdin.readline

n = int(input())
stairs = []
dp = []
for i in range(n):
    stairs.append(int(input()))

# 바로 최댓값을 출력해서 끝내도 됨
if n==1:
    print(stairs[0])
    exit()
elif n == 2:
    print(max(stairs[0]+stairs[1], stairs[1]))
    exit()

dp.append(stairs[0])
dp.append(max(dp[0]+stairs[1], stairs[1]))
dp.append(max(dp[0]+stairs[2], stairs[1]+stairs[2]))

for i in range(3, n):
    dp.append(max(dp[i-2]+stairs[i], dp[i-3]+stairs[i-1]+stairs[i]))

print(dp[-1])

# 출처: https://jainn.tistory.com/83 [Dogfootruler Kim:티스토리]