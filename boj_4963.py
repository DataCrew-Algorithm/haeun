# Island
# 정사각형 (땅 위치)와 연결이 가능한 사각형: 가로-세로-대각선 연결

import sys
read = sys.stdin.readline

# Ver1.
# def dfs(x, y):
    
#     dx = [-1, 1, 0, 0, -1, -1, 1, 1]  # 상하, 대각선
#     dy = [0, 0, -1, 1, -1, 1, -1, 1]  # 좌우, 대각선

#     for i in range(8): # 대각선 고려
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if graph[ny][nx] == 1: # 땅이면, 상하좌우대각선 확인
#             print(graph[ny][nx])
#             graph[ny][nx] = -1
#             dfs(x, y)
#             return 1
#     return 0

# Flag = True

# while Flag:
#     w, h = map(int, input().split())

#     if w == 0 and h == 0:
#         break
#     else:
#         graph = []
#         for i in range(h):
#             graph.append(list(map(int, read().split())))
#         print(graph) # [[1, 0, 1, 0, 1], [0, 0, 0, 0, 0], [1, 0, 1, 0, 1], [0, 0, 0, 0, 0], [1, 0, 1, 0, 1]]

#         cnt = 0
#         for i in range(h):
#             for j in range(w):
#                 if graph[i][j] == 1: # 재귀적으로 호출하여 1이 있는 구역 세기
#                     cnt += 1 
#         print(cnt)


# Ver2.
# from collections import deque

# dx = [-1, 1, 0, 0, -1, -1, 1, 1]  # 상하, 대각선
# dy = [0, 0, -1, 1, -1, 1, -1, 1]  # 좌우, 대각선

# def bfs(x, y):
#     q = deque([x, y])
#     while q:
#         x, y = q.popleft()

#         for i in range(8): # 대각선 고려
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1: # 1 표시가 되어 있는 위치이면,
#                 graph[nx][ny] = 0 # 방문 표시 1 이 아닌 수
#                 q.append([nx, ny])


# Flag = True

# while Flag:
#     w, h = map(int, input().split())

#     if w == 0 and h == 0:
#         break
#     else:
#         graph = []
#         for i in range(h):
#             graph.append(list(map(int, read().split())))
#         print(graph)

#         # print(graph)
#         cnt = 0
#         for i in range(h):
#             for j in range(w):
#                 if graph[i][j] == 1:
#                     bfs(i, j)  # 재귀적으로 호출하여 1이 있는 구역 세기
#                     cnt += 1

#         print(cnt)

# Ver3.
import sys
sys.setrecursionlimit(100)
def dfs(x, y):

    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < w) and (0 <= ny < h):
            if graph[ny][nx] == 1:
                graph[ny][nx] = -1
                dfs(nx, ny)

while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 & h ==0:
        break
    else:
        graph =[]
        for _ in range(h):
            tmp = list(map(int, sys.stdin.readline().split()))
            graph.append(tmp)

        cnt = 0

        for y in range(h):
            for x in range(w):
                if graph[y][x] == 1:
                    dfs(x, y)
                    cnt += 1
        # print(graph)

        print(cnt)
    