# Organic Cabbage
# import sys
# from collections import deque

# T = int(input())

# dx = [-1, 1, 0, 0] 
# dy = [0, 0, -1, 1]

# for _ in range(T):
#     M, N, K = map(int, input().split())

#     graph = [[0]*(M) for _ in range(N)] # M * N 행렬    
 
#     for i in range(K):
#         x, y = [int(i) for i in sys.stdin.readline().split()]
#         graph[y][x] = 1

#     # v = [[False]*M for _ in range(N)]

#     result = 0
#     for i in range(N):
#         for j in range(M):
#             q = deque()

#             if v[j][i] == True or graph[j][i] == 0: # list index out of range
#                 continue

#             v[i][j] = result
#             q.append((i, j))

#             while q:
#                 x, y = q.popleft()
#                 v[y][x] = True

#                 # 현재 위치에서 상하좌우 위치 확인
#                 for i in range(4):
#                         cx, cy = x + dx[i], y + dy[i]
#                         if 0 <= cy < N and 0 <= cx < M:
#                             if v[cy][cx] == False and graph[cy][cx] == 1:
#                                 q.append((cx, cy))
#                                 v[cy][cx] = True
#             result += 1

#     print(result)


# 참고 풀이 버전: 재귀함수 호출 가능하고, 좌표 위치 직접 확인할 것

import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y):
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1: # 1 표시가 되어 있는 위치이면,
                q.append((nx, ny))
                graph[nx][ny] = 2 # 왜 2일까?? => 방문 표시를 위함이므로 1 이 아닌 수면 상관없음!
    return 1


for _ in range(int(sys.stdin.readline())):
    m, n, k = map(int, sys.stdin.readline().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]

    dx = [-1, 1, 0, 0]  # 상하
    dy = [0, 0, -1, 1]  # 좌우

    for i in range(k):
        a, b = map(int, sys.stdin.readline().split())
        graph[b][a] = 1

    # print(graph)
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                cnt += bfs(i, j)  # 재귀적으로 호출하여 1이 있는 구역 세기

    print(cnt)