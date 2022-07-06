# Friends
# 가장 유명한 사람의 2-친구수?? 를 구해라
# 구조적 대칭 무방향 그래프 (네트워크)

# import sys
# read = sys.stdin.readline

# N = int(input())
# graph = [list(read().rstrip()) for _ in range(N)]
# print(graph)

# visited = [0 for _ in range(N)]

# # 깊이 우선 탐색
# def dfs(x):
#     for i in range(N):
#       if graph[x][i] == 'Y' and visited[i] == 0: # 시작점 x에서 i번째 숫자가 1이고, 방문 처리 안 되어 있으면
#         visited[i] = 1 # 방문 처리
#         dfs(i) # i가 시작점이 되어 연결 지점 탐색

# # 1과 0으로 바꿔서 보려고 코드 그대로 사용.. (탐색이 끝나면 연결 정보에 따라 1, 0 출력)
# for i in range(N):
#     dfs(i)
#     for j in range(N):
#         # print(visited)
#         if visited[j] == 1:
#             print(1, end=" ")
#         else:
#             print(0, end=" ")          
#     print()
#     visited = [0 for _ in range(N)] # 초기화


# 2-친구 수의 의미를 정확히 파악하지 못해서 참고한 풀이를 bfs로 변형함
# edge가 2개 이상인 친구 중 제일 많이 방문할 수 있는 노드를 찾는 방식으로 풀기

# import sys
# read = sys.stdin.readline

# N = int(input())
# graph = [list(read().rstrip()) for _ in range(N)]
# print(graph)

# def dfs(v):
#     visited = [False for _ in range(N)]
#     visited[v] = True
#     stk = [(v, 0)] # 시작 노드와 깊이 지정

#     cnt = -1

import sys
read = sys.stdin.readline

N = int(input())
board = [list(read().rstrip()) for _ in range(N)]

def bfs(x):
    visited = [False for _ in range(N)]
    visited[x] = True
    # print(visited)
    stk = [(x, 0)]
    cnt = -1

    while stk:
        current_x, depth = stk.pop()

        for i in range(N):
            if board[current_x][i] == "Y" and visited[i] == 0: # 새로운 정점에서 다른 정점 연결되었는지 탐색
                if depth <2:
                    # print(stk)
                    stk.append((i, depth+1))  # 연결 edge가 2개가 안될 때 위 조건을 만족하니까 +1
                    visited[i] = True # 방문 처리
        
        cnt += 1 # 친구 수 누적
    return cnt

ans = -1
for i in range(N):
    friend = bfs(i)
    # print(friend) # 친구 수 맞게 나오는지 확인
    ans = max(ans, friend)

print(ans)
