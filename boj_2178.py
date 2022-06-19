# Maze
# 서로 인접한 방향으로만 이동 가능 / 최소 이동 칸 수??
# 132ms -> 108 ms (sys module)
import sys
from collections import deque

read = sys.stdin.readline

n, m = map(int, input().split())

# 미로 맵 입력
graph = []
for _ in range(n):
    graph.append(list(map(int, read().rstrip())))

# print(graph)

# 상하좌우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 로 미로 길 찾기
def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        # 현재 위치에서 4가지 인접 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            # 미로 공간을 벗어나면 무시
            if nx >= n or ny >= m or nx < 0 or ny < 0:
                continue
            
            # 인접 좌표가 벽, 0이면 무시
            if graph[nx][ny] == 0:
                continue

            # 해당 노드를 처음 방문하는 경우에만 queue에 방문 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1 # 1칸 이동
                queue.append((nx, ny))

    # 가장 오른쪽 아래까지 최단 거리 반환
    return graph[n-1][m-1]
print(bfs(0, 0))
