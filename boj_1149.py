# RGB 거리
# 모든 집을 색칠하는 최소비용 구하기

# import sys

# 집의 개수 및 페인트 색 비용 입력
# N = int(input())
# colors = []
# for _ in range(N):
#     r, g, b = list(map(int, sys.stdin.readline().split()))
#     colors.append([r, g, b])
# print(colors)

# costs = []
# for i in range(len(colors) - 1):
#     red = colors[i][0]
#     green = colors[i][1]
#     blue = colors[i][2]

#     cost = min(colors[i])

    # if colors[i].index(cost) == colors[i+1].index(min(colors[i+1])): # 최솟값의 위치가 같은지 판단
    #     costs.append(min(colors[i][i+1:])) # TypeError: 'int' object is not iterable & min arg() is empty

    # print(cost)
    # print(costs)
# print(sum(costs))


# 매트릭스 활용하기 (116ms, 풀이 참고: https://chunghyup.tistory.com/48) 
def min(a, b):
    return a if a <= b else b

n = int(input())
homes = [[0]*3 for _ in range(n)]
for i in range(n):
    homes[i][0], homes[i][1], homes[i][2] = map(int, input().split())
# print(homes) -- 여기까지 같음

painted_homes = [[0]*3 for _ in range(n)]

for i in range(n):
    if i == 0:
        painted_homes[i] = homes[i]
    else:
        # 위치에 각각 이전 행이랑 비교해 최솟값으로 업데이트 // 누적으로 더해서 체크
        painted_homes[i][0] = homes[i][0] + min(painted_homes[i-1][1], painted_homes[i-1][2])
        painted_homes[i][1] = homes[i][1] + min(painted_homes[i-1][0], painted_homes[i-1][2])
        painted_homes[i][2] = homes[i][2] + min(painted_homes[i-1][0], painted_homes[i-1][1])
print(painted_homes)
print(min(min(painted_homes[n-1][0], painted_homes[n-1][1]), painted_homes[n-1][2]))


