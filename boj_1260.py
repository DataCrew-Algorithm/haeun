# DFS와 BFS

# from collections import deque
# import sys
# sys.setrecursionlimit(10**7) # RecursionError 방지

# n, m, v = map(int, sys.stdin.readline().split())
# graph = [[False] * (n + 1) for _ in range(n + 1)]
# visited = [False]*(n+1)

# for _ in range(m):
#     a, b = map(int, sys.stdin.readline().split())
#     graph[a][b] = graph[b][a] = True # 노드로 연결된 것을 표시

# def dfs(v):
#       if not visited[v]:
#         visited[v] = True
#         print(v, end=" ")
#         for i in range(1, n+1):
#           if graph[v][i] == True:
#             dfs(v)

# def bfs(v):
#     queue= deque([v])
#     visited[v] = False

#     # 큐가 빌때까지 반복
#     while queue:
#       v = queue.popleft()
#       print(v, end=' ')

#       # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
#       for i in range(1, n+1):
#           if (visited[i] == True and graph[v][i] == True):
#             queue.append(i)

# dfs(v)
# print()
# bfs(v)

ver2
from collections import deque

N, M, V = map(int, input().split())

graph = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
  m1, m2 = map(int, input().split())
  # 노드 연결 하기
  graph[m1][m2] = graph[m2][m1] = 1

# 너비 우선 탐색
def bfs(start_v):
  discoverd = [start_v]
  queue = deque() 
  queue.append(start_v)

  while queue:
    v = queue.popleft()
    print(v, end=' ')

    for w in range(len(graph[start_v])):
      if graph[v][w] == 1 and (w not in discoverd):
        discoverd.append(w)
        queue.append(w)

# 깊이 우선 탐색
def dfs(start_v, discoverd=[]):
  discoverd.append(start_v)
  print(start_v, end=' ')

  for w in range(len(graph[start_v])):
    if graph[start_v][w] == 1 and (w not in discoverd):
      dfs(w, discoverd)

dfs(V)
print()
bfs(V)