# Jump King Jelly
# 젤리가 정사각형 게임판에서 가장 우측 아래 칸으로 이동하면 승리
# 게임 구역 크기 2<= N <= 3
# 한번에 이동 가능한 칸 수: 현재 밟고 있는 칸에 적힌 수 만큼 (0~100이하 정수)
# from collections import deque

N = int(input())

# 2차원 맵 정보 입력 받기

graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

# print(graph) # [[2, 2, 1], [2, 2, 2], [1, 2, -1]]

# 이동 가능한 방향 (오른쪽, 아래)
dx = [0, 1, 0, 0]
dy = [0, 0, 0, 1]

# BFS 구현

def bfs(x, y):
    # 큐 구현을 위해 deque 사용
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        #현재 위치에서 2가지 방향 이동 위치확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
        # 처음 이동가능한 칸의 수의 합이 가로 길이까지 다음 이동 가능
        # if graph[nx][ny] + x <= N and graph[nx][ny] + y <= N:
        if graph[nx][ny] + [x] <= N and graph[nx][ny] + [y] <= N: # 하면 append와 같은 효과!   
            # graph[nx] = list(graph[nx] + x) # TypeError: can only concatenate list (not "int") to list
            # graph[ny] = list(graph[ny] + y)
            graph[nx].append(x) 
            graph[ny].append(y) # IndexError: list index out of range
            queue.append((nx, ny)) 
        else:
            print('Hing') 

    if graph[nx][ny] == graph[N-1][N-1]:
        print('HaruHaru') 

print(bfs(0, 0))



# 참고 풀이 (96ms)
from collections import deque
 
n = int(input())
 
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))
 
visited = []
for _ in range(n):
    visited.append([False]*n)

# 2가지 방향만 가능해서 2X2 로 가능
dx = [1, 0]
dy = [0, 1]
 
 
def bfs(x, y, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
 
    while queue:
        x, y = queue.popleft()
        if array[x][y] == -1: # 마지막 도착지점에 도착하면 바로 리턴
            return 'HaruHaru'
        for i in range(2):
            nx = x + dx[i] * array[x][y] # 점프하는거라서 곱하기
            ny = y + dy[i] * array[x][y]

            if nx < 0 or ny < 0 or nx >= n or ny >= n: # 문제에서 벗어날일 없다고 해서 추가 안 했는데 안 하면 index error남
                continue
            if visited[nx][ny] == True:
                continue
            if visited[nx][ny] == False:
                visited[nx][ny] = True
                queue.append((nx, ny))

        print(visited)
    return 'Hing'
 
print(bfs(0, 0, visited))


# Ver3: True, False -> 1, 0로 변경해서 확인
# from collections import deque
 
# n = int(input())
 
# array = []
# for _ in range(n):
#     array.append(list(map(int, input().split())))
 
# visited = []
# for _ in range(n):
#     visited.append([0]*n)

# # 2가지 방향만 가능해서 2X2 로 가능
# dx = [1, 0]
# dy = [0, 1]
 
 
# def bfs(x, y, visited):
#     queue = deque()
#     queue.append((x, y))
#     visited[x][y] = 1
 
#     while queue:
#         x, y = queue.popleft()
#         if array[x][y] == -1: # 마지막 도착지점에 도착하면 바로 리턴
#             return 'HaruHaru'
#         for i in range(2):
#             nx = x + dx[i] * array[x][y] # 점프하는거라서 곱하기
#             ny = y + dy[i] * array[x][y]

#             if nx < 0 or ny < 0 or nx >= n or ny >= n: # 문제에서 벗어날일 없다고 해서 추가 안 했는데 안 하면 index error남
#                 continue
#             if visited[nx][ny] == 1:
#                 continue
#             if visited[nx][ny] == 0:
#                 visited[nx][ny] = 1
#                 queue.append((nx, ny))
                
#         print(visited)
#     return 'Hing'
 
# print(bfs(0, 0, visited))