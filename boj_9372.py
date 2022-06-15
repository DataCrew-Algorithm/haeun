# Travel
# ver1. 1084ms
# from sys import stdin
# read = stdin.readline

# def dfs(start, dic):
#     for i in dic[start]:
#         if i not in visited: # in & not_in 함수는 효율이 안 좋을 수 밖에..
#             visited.append(i)
#             dfs(i, dic)

# T = int(read())
# for _ in range(T):
#     N, M = map(int, read().split()) # 국가 수, 비행기 종류
#     dic={}
#     for i in range(N):
#         dic[i+1] = set()
#     for j in range(M):
#         a, b = map(int,read().split())
#         dic[a].add(b)
#         dic[b].add(a)
    # print(dic)
#     # {1: {2, 3}, 2: {1, 3}, 3: {1, 2}}
#     # {1: {2}, 2: {1, 3}, 3: {2, 4}, 4: {3, 5}, 5: {4}}

#     visited = []
#     dfs(1, dic)
#     print(len(visited)-1) # 최소 비행 편 수는 방문국가 수 - 1

# ver2. 1104ms
# from collections import deque
# from sys import stdin
# read = stdin.readline

# def dfs(graph, start_node):
#     need_visited, visited = deque(), deque()
#     need_visited.append(start_node)
    
#     ## 만약 아직도 방문이 필요한 노드가 있다면,
#     while need_visited:
 
#         ## 그 중에서 가장 마지막 데이터를 추출
#         node = need_visited.pop()
        
#         ## 만약 그 노드가 방문한 목록에 없다면
#         if node not in visited:
 
#             ## 방문한 목록에 추가하기 
#             visited.append(node)
 
#             ## 그 노드에 연결된 노드를 방문 예정 리스트에 추가
#             need_visited.extend(graph[node])
            
#     return len(visited)-1

# T = int(read())
# for _ in range(T):
#     N, M = map(int, read().split()) # 국가 수, 비행기 종류

#     graph={}
#     for i in range(N):
#         graph[i+1] = set()
#     for j in range(M):
#         a, b = map(int,read().split())
#         graph[a].append(b)
#         graph[b].append(a)
#     print(graph)
#     print(dfs(graph,1))


#ver3. 1108ms
# from collections import defaultdict, deque
# from sys import stdin
# read = stdin.readline

# def dfs(graph, start_node):
#     need_visited, visited = deque(), deque()
#     need_visited.append(start_node)
    
#     while need_visited:
#         node = need_visited.pop()

#         if node not in visited: 
#             visited.append(node)
#             need_visited.extend(graph[node])
            
#     return len(visited)-1

# T = int(read())
# for _ in range(T):
#     N, M = map(int, read().split()) # 국가 수, 비행기 종류
#     graph = defaultdict(list)

#     for j in range(M):
#         a, b = map(int,read().split())
#         graph[a].append(b)
#         graph[b].append(a)
#     # print(graph)
#     # defaultdict(<class 'list'>, {1: [2, 3], 2: [1, 3], 3: [2, 1]})
#     # defaultdict(<class 'list'>, {2: [1, 3], 1: [2], 3: [2, 4], 4: [3, 5], 5: [4]})
#     print(dfs(graph,1))

# ver4. 176ms // 바로 국가 연결되어 있어서 -1하면 된다..! (무방향 그래프)
from sys import stdin
read = stdin.readline

T = int(read())
for _ in range(T):
    N, M = map(int, read().split()) # 국가 수, 비행기 종류
    
    for j in range(M):
        a, b = map(int,read().split())
    print(N-1)
