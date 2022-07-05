# 경로 찾기: 모든 정점에서 가는 경로가 있는 지 없는지 구하기
# 인접 행렬 형태로 출력!

# 풀이 (144ms)
import sys
read = sys.stdin.readline

N = int(input())

graph = []
for _ in range(N):
    graph.append(list(map(int, read().split())))
# print(graph)

visited = [0 for _ in range(N)]

# 깊이 우선 탐색
def dfs(x):
    for i in range(N):
      if graph[x][i] == 1 and visited[i] == 0: # 시작점 x에서 i번째 숫자가 1이고, 방문 처리 안 되어 있으면
        visited[i] = 1 # 방문 처리
        dfs(i) # i가 시작점이 되어 연결 지점 탐색

# 탐색이 끝나면 연결 정보에 따라 1, 0 출력
for i in range(N):
    dfs(i)
    for j in range(N):
        # print(visited)
        if visited[j] == 1:
            print(1, end=" ")
        else:
            print(0, end=" ")          
    print()
    visited = [0 for _ in range(N)] # 초기화


# bfs 참고 풀이 (176ms)
# => 최초 시작점을 기준으로 계속 visited에 기록해야 함 (주의!!)
from collections import deque
import sys
read = sys.stdin.readline

N = int(input())
graph = [list(map(int, read().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)] # 이중 리스트
queue = deque()

def bfs(x):
  check = [0 for _ in range(N)]

  while queue:
    nx = queue.popleft()

    for i in range(N):
        if graph[nx][i] == 1 and check[i] == 0: # 새로운 정점에서 다른 정점 연결되었는지 탐색
          queue.append(i)
          check[i] = 1
          visited[x][i] = 1 # 방문 처리
          
for i in range(N):
      queue.append(i)
      bfs(i)
    
for v in visited:
      print(*v) # 언패킹 해주기


