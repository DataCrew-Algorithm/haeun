# 단지 번호붙이기 (Numbering Building blocks)

# ver1. 예제는 맞는데 틀림
# import sys
# sys.setrecursionlimit(1000)
# read = sys.stdin.readline


# def dfs(x, y):
#     building_num = 0

#     dx = [-1, 1, 0, 0]  # 상하
#     dy = [0, 0, -1, 1]  # 좌우

#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if (0 <= nx < n) and (0 <= ny < n): # 지도 범위 내 위치가 아니면
#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = -1
#                 # print(dfs(nx, ny)) # 정수형 타입으로 찍어준다??
#                 building_num += dfs(nx, ny) # 1-> -1로 바뀌고 나서 빌딩 개수를 더해주기

#     return  building_num + 1


# n = int(input())

# graph = []
# for _ in range(n):
#     graph.append(list(map(int, read().rstrip())))
# # print(graph)

# buildings = []
# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 1:
#             buildings.append(dfs(i, j))  # 재귀적으로 호출하여 1이 있는 구역 세기

# buildings.sort()
# print(len(buildings)) # 구역 개수
# for i in buildings: # 각 구역 내 빌딩 수
#     print(i - 1)



# map = [[0, -1, -1, 0, 1, 0, 0], [0, -1, -1, 0, 1, 0, 1], [-1, -1, -1, 0, 1, 0, 1]]

# buildings = []
# for a in range(len(map)):
#     building = map[a].count(-1)
#     buildings.append(building)
#     # for b in range(7):
#     #     print(map[a][b])
# print(buildings)


# ver2. 방문처리 해주기 (76ms)

# import sys
# sys.setrecursionlimit(1000)
# read = sys.stdin.readline

def dfs(x, y, group):
    visited[x][y] = 1
    graph[x][y] = group
    count[group] += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
     
        if (0 <= nx < n) and (0 <= ny < n):
           if graph[nx][ny] and visited[nx][ny] == 0:
            dfs(nx, ny, group)


n = int(input())

graph = [list(map(int, input())) for _ in range(n)] # readline으로 하면 rstrip 해줘야 함
visited = [[0 for _ in range(n)] for _ in range(n)] # 이중 리스트로
group = 0

# print(graph)

dx = [-1, 1, 0, 0]  # 상하
dy = [0, 0, -1, 1]  # 좌우
count = [0] * (n*n+1) # 0부터 남기려고 n*n+1 형태

for i in range(n):
    for j in range(n):
        if graph[i][j] and visited[i][j] == 0:
            dfs(i, j, group)  # 재귀적으로 호출하여 1이 있는 구역 세기
            group += 1

count.sort()
print(group)
# print(count) # 그룹 인덱스로 잡힌 빌딩 수
for i in count:
    if i > 0 :
        print(i)